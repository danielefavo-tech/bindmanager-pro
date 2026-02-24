"""BINDMANAGER PRO — Backend FastAPI"""
import os, io, logging, threading
from typing import Optional
from fastapi import FastAPI, Depends, HTTPException, UploadFile, File, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database import engine, get_db, SessionLocal
from app import models
from app.auth import hash_password, verify_password, create_token, get_current_user, require_admin
from app.import_excel import row_to_prodotto
from app.ai_claude import genera_descrizione_claude, genera_descrizione_libro

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="BindManager Pro", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True,
                   allow_methods=["*"], allow_headers=["*"])

# Stato import globale in memoria
_job = {"running": False, "importati": 0, "aggiornati": 0, "errori": [],
        "skippati": 0, "totale": 0, "completato": False, "messaggio": ""}

@app.on_event("startup")
def startup():
    models.Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        if not db.query(models.User).filter(models.User.ruolo == "admin").first():
            db.add(models.User(email="admin@bindmanager.it", nome="Daniele",
                               hashed_password=hash_password("bindmanager2024"), ruolo="admin"))
            db.commit()
    finally:
        db.close()

static_dir = os.path.join(os.path.dirname(__file__), "..", "static")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

class UserCreate(BaseModel):
    email: str; nome: str; password: str; ruolo: str = "collaboratore"

class ProdottoUpdate(BaseModel):
    titolo: Optional[str] = None; descrizione: Optional[str] = None
    prezzo_vendita: Optional[float] = None; quantita: Optional[int] = None
    stato_bene: Optional[str] = None; tag: Optional[str] = None

class ConfigSet(BaseModel):
    chiave: str; valore: str

def _get_config(db, chiave, default=""):
    c = db.query(models.Configurazione).filter(models.Configurazione.chiave == chiave).first()
    return c.valore if c else default

def _set_config(db, chiave, valore):
    c = db.query(models.Configurazione).filter(models.Configurazione.chiave == chiave).first()
    if c: c.valore = valore
    else: db.add(models.Configurazione(chiave=chiave, valore=valore))
    db.commit()

def _log(db, operazione, dettaglio, livello="info", utente=""):
    try:
        db.add(models.Log(operazione=operazione, dettaglio=dettaglio,
                          livello=livello, utente_email=utente))
        db.commit()
    except: pass

# ── PING ───────────────────────────────────────────────────────
@app.get("/api/ping")
def ping(db: Session = Depends(get_db)):
    return {"status": "ok", "prodotti_nel_db": db.query(models.Prodotto).count(),
            "utenti": db.query(models.User).count()}

# ── AUTH ───────────────────────────────────────────────────────
@app.post("/api/auth/login")
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == form.username).first()
    if not user or not verify_password(form.password, user.hashed_password):
        raise HTTPException(401, "Credenziali non valide")
    if not user.attivo:
        raise HTTPException(403, "Account disattivato")
    token = create_token({"sub": user.email, "ruolo": user.ruolo})
    return {"access_token": token, "token_type": "bearer",
            "nome": user.nome, "ruolo": user.ruolo, "email": user.email}

@app.get("/api/auth/me")
def me(current_user=Depends(get_current_user)):
    return {"email": current_user.email, "nome": current_user.nome, "ruolo": current_user.ruolo}

# ── DASHBOARD ──────────────────────────────────────────────────
@app.get("/api/dashboard")
def dashboard(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    totale = db.query(models.Prodotto).count()
    return {
        "totale": totale,
        "esauriti": db.query(models.Prodotto).filter(models.Prodotto.quantita == 0).count(),
        "sottoscorta": db.query(models.Prodotto).filter(models.Prodotto.quantita > 0, models.Prodotto.quantita <= 2).count(),
        "con_ai": db.query(models.Prodotto).filter(models.Prodotto.ai_generata == True).count(),
        "inviati_bc": db.query(models.Prodotto).filter(models.Prodotto.bindcommerce_inviato == True).count(),
        "con_foto": db.query(models.Prodotto).filter(models.Prodotto.foto1 != None, models.Prodotto.foto1 != "").count(),
        "logs": [{"operazione": l.operazione, "dettaglio": l.dettaglio, "livello": l.livello,
                  "data": l.creato_il.isoformat() if l.creato_il else ""}
                 for l in db.query(models.Log).order_by(models.Log.creato_il.desc()).limit(20).all()]
    }

# ── PRODOTTI ───────────────────────────────────────────────────
@app.get("/api/prodotti")
def lista_prodotti(page: int = 1, per_page: int = 50, cerca: str = "",
                   categoria: str = "", stato: str = "",
                   solo_esauriti: bool = False, solo_senza_ai: bool = False,
                   db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    q = db.query(models.Prodotto)
    if cerca:
        like = f"%{cerca}%"
        q = q.filter(models.Prodotto.titolo.ilike(like) | models.Prodotto.codice.ilike(like) |
                     models.Prodotto.ean.ilike(like) | models.Prodotto.autore.ilike(like))
    if categoria: q = q.filter(models.Prodotto.categoria1.ilike(f"%{categoria}%"))
    if stato: q = q.filter(models.Prodotto.stato_bene == stato)
    if solo_esauriti: q = q.filter(models.Prodotto.quantita == 0)
    if solo_senza_ai: q = q.filter(models.Prodotto.ai_generata == False)
    totale = q.count()
    prodotti = q.order_by(models.Prodotto.id.desc()).offset((page-1)*per_page).limit(per_page).all()
    return {
        "totale": totale,
        "pagine": max(1, (totale + per_page - 1) // per_page),
        "pagina": page,
        "prodotti": [{"id": p.id, "codice": p.codice, "ean": p.ean, "titolo": p.titolo,
                      "autore": p.autore, "anno": p.anno, "categoria1": p.categoria1,
                      "categoria2": p.categoria2, "produttore": p.produttore,
                      "stato_bene": p.stato_bene, "prezzo_vendita": p.prezzo_vendita,
                      "quantita": p.quantita, "foto1": p.foto1, "ai_generata": p.ai_generata,
                      "bindcommerce_inviato": p.bindcommerce_inviato,
                      "posizione_magazzino": p.posizione_magazzino} for p in prodotti]
    }

@app.get("/api/prodotti/{prodotto_id}")
def get_prodotto(prodotto_id: int, db: Session = Depends(get_db),
                 current_user=Depends(get_current_user)):
    p = db.query(models.Prodotto).filter(models.Prodotto.id == prodotto_id).first()
    if not p: raise HTTPException(404, "Prodotto non trovato")
    return {"id": p.id, "codice": p.codice, "ean": p.ean, "titolo": p.titolo,
            "autore": p.autore, "anno": p.anno, "categoria1": p.categoria1,
            "categoria2": p.categoria2, "tipo_prodotto": p.tipo_prodotto,
            "produttore": p.produttore, "stato_bene": p.stato_bene,
            "specifiche": p.specifiche, "prezzo_vendita": p.prezzo_vendita,
            "quantita": p.quantita, "posizione_magazzino": p.posizione_magazzino,
            "descrizione_breve": p.descrizione_breve, "descrizione": p.descrizione,
            "descrizione_sito": p.descrizione_sito, "note": p.note, "tag": p.tag,
            "foto1": p.foto1, "foto2": p.foto2, "foto3": p.foto3,
            "ai_generata": p.ai_generata, "bindcommerce_inviato": p.bindcommerce_inviato}

@app.patch("/api/prodotti/{prodotto_id}")
def aggiorna_prodotto(prodotto_id: int, data: ProdottoUpdate,
                      db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    p = db.query(models.Prodotto).filter(models.Prodotto.id == prodotto_id).first()
    if not p: raise HTTPException(404, "Prodotto non trovato")
    for k, v in data.dict(exclude_none=True).items():
        setattr(p, k, v)
    db.commit()
    return {"ok": True}

# ── IMPORT EXCEL (background thread) ──────────────────────────
def _run_import(file_bytes: bytes, modalita: str, utente_email: str):
    global _job
    from openpyxl import load_workbook
    _job = {"running": True, "importati": 0, "aggiornati": 0, "errori": [],
            "skippati": 0, "totale": 0, "completato": False, "messaggio": "Lettura file..."}
    try:
        wb = load_workbook(io.BytesIO(file_bytes), read_only=True, data_only=True)
        ws = wb.active
        rows = list(ws.iter_rows(min_row=2, values_only=True))
        _job["totale"] = len(rows)
        _job["messaggio"] = f"Elaborazione {len(rows)} prodotti..."
        logger.info(f"Import background: {len(rows)} righe, modalita={modalita}")

        db = SessionLocal()
        try:
            BATCH = 200
            for i, row in enumerate(rows):
                try:
                    prod = row_to_prodotto(row)
                    if not prod:
                        _job["skippati"] += 1
                        continue
                    codice = str(prod.get("codice", "")).strip()
                    esistente = db.query(models.Prodotto).filter(
                        models.Prodotto.codice == codice).first() if codice else None

                    if esistente:
                        if modalita in ("aggiorna", "entrambi"):
                            esistente.quantita = prod.get("quantita", esistente.quantita)
                            esistente.prezzo_vendita = prod.get("prezzo_vendita", esistente.prezzo_vendita)
                            if prod.get("stato_bene"): esistente.stato_bene = prod["stato_bene"]
                            if prod.get("titolo"): esistente.titolo = prod["titolo"]
                            if prod.get("foto1") and not esistente.foto1: esistente.foto1 = prod["foto1"]
                            _job["aggiornati"] += 1
                        else:
                            _job["skippati"] += 1
                    else:
                        if modalita in ("nuovi", "entrambi"):
                            db.add(models.Prodotto(**prod))
                            _job["importati"] += 1

                    if (i + 1) % BATCH == 0:
                        db.commit()
                        _job["messaggio"] = f"Elaborati {i+1}/{len(rows)}..."
                        logger.info(f"Import: {i+1}/{len(rows)}")

                except Exception as e:
                    try: db.rollback()
                    except: pass
                    _job["errori"].append(f"Riga {i+2}: {str(e)[:80]}")
                    if len(_job["errori"]) > 30: break

            db.commit()
            _log(db, "Import Excel",
                 f"Importati: {_job['importati']}, Aggiornati: {_job['aggiornati']}, "
                 f"Errori: {len(_job['errori'])}", "success", utente_email)
        finally:
            db.close()

    except Exception as e:
        logger.error(f"Import error: {e}")
        _job["errori"].append(str(e)[:100])

    _job["running"] = False
    _job["completato"] = True
    _job["messaggio"] = f"✅ Completato! Nuovi: {_job['importati']}, Aggiornati: {_job['aggiornati']}"
    logger.info(_job["messaggio"])


@app.post("/api/import/excel")
async def import_excel(
    file: UploadFile = File(...),
    modalita: str = Form("entrambi"),
    genera_ai: bool = Form(False),
    current_user=Depends(get_current_user)
):
    global _job
    if _job["running"]:
        raise HTTPException(400, "Import già in corso, aspetta che finisca")
    content = await file.read()
    logger.info(f"File ricevuto: {file.filename}, {len(content)} bytes")
    t = threading.Thread(target=_run_import, args=(content, modalita, current_user.email), daemon=True)
    t.start()
    return {"ok": True, "messaggio": "Import avviato in background"}

@app.get("/api/import/status")
def import_status(current_user=Depends(get_current_user)):
    return _job

# ── AI ─────────────────────────────────────────────────────────
@app.post("/api/prodotti/{prodotto_id}/genera-ai")
def genera_ai_prodotto(prodotto_id: int, db: Session = Depends(get_db),
                       current_user=Depends(get_current_user)):
    p = db.query(models.Prodotto).filter(models.Prodotto.id == prodotto_id).first()
    if not p: raise HTTPException(404, "Prodotto non trovato")
    api_key = _get_config(db, "claude_api_key")
    if not api_key: raise HTTPException(400, "API Key Claude non configurata")
    cat1 = (p.categoria1 or "").lower()
    if cat1 in ("cd", "dischi vinile 33 giri", "dischi vinile 45 giri", "musicassette"):
        ai_data = genera_descrizione_claude(
            artista=p.autore or "", album=p.titolo or "", anno=p.anno or "",
            label=p.produttore or "", generi=cat1, stili="", tracklist="", paese="",
            stato_fisico=p.stato_bene or "", specifiche=p.specifiche or "", api_key=api_key)
    else:
        ai_data = genera_descrizione_libro(titolo=p.titolo or "", autore=p.autore or "",
            anno=p.anno or "", editore=p.produttore or "", stato=p.stato_bene or "", api_key=api_key)
    if not ai_data: raise HTTPException(500, "Claude non ha risposto. Verifica la API Key.")
    p.descrizione = ai_data.get("ebay_description", "")
    p.descrizione_sito = ai_data.get("sito_description", "")
    tags_extra = ai_data.get("tags_extra", [])
    if tags_extra: p.tag = (p.tag or "") + (", " if p.tag else "") + ", ".join(tags_extra)
    p.ai_generata = True
    db.commit()
    _log(db, "AI Generata", f"{p.codice} — {(p.titolo or '')[:50]}", "success", current_user.email)
    return {"ok": True, "descrizione": p.descrizione, "tag": p.tag}

# ── CONFIG ─────────────────────────────────────────────────────
@app.get("/api/config")
def get_config(db: Session = Depends(get_db), current_user=Depends(require_admin)):
    keys = ["claude_api_key", "bindcommerce_api_key", "sync_interval"]
    result = {}
    for k in keys:
        v = _get_config(db, k)
        result[k] = (v[:8] + "..." + v[-4:] if len(v) > 12 else "****") if "api_key" in k and v else v
    return result

@app.post("/api/config")
def set_config(data: ConfigSet, db: Session = Depends(get_db), current_user=Depends(require_admin)):
    _set_config(db, data.chiave, data.valore)
    _log(db, "Config", f"Chiave: {data.chiave}", "info", current_user.email)
    return {"ok": True}

# ── UTENTI ─────────────────────────────────────────────────────
@app.get("/api/utenti")
def lista_utenti(db: Session = Depends(get_db), current_user=Depends(require_admin)):
    return [{"id": u.id, "email": u.email, "nome": u.nome, "ruolo": u.ruolo, "attivo": u.attivo}
            for u in db.query(models.User).all()]

@app.post("/api/utenti")
def crea_utente(data: UserCreate, db: Session = Depends(get_db), current_user=Depends(require_admin)):
    if db.query(models.User).filter(models.User.email == data.email).first():
        raise HTTPException(400, "Email già registrata")
    db.add(models.User(email=data.email, nome=data.nome, ruolo=data.ruolo,
                       hashed_password=hash_password(data.password)))
    db.commit()
    return {"ok": True}

@app.delete("/api/utenti/{user_id}")
def elimina_utente(user_id: int, db: Session = Depends(get_db), current_user=Depends(require_admin)):
    u = db.query(models.User).filter(models.User.id == user_id).first()
    if not u: raise HTTPException(404, "Utente non trovato")
    if u.email == current_user.email: raise HTTPException(400, "Non puoi eliminare te stesso")
    db.delete(u); db.commit()
    return {"ok": True}

# ── LOG ────────────────────────────────────────────────────────
@app.get("/api/logs")
def get_logs(limit: int = 100, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return [{"id": l.id, "operazione": l.operazione, "dettaglio": l.dettaglio,
             "livello": l.livello, "utente": l.utente_email,
             "data": l.creato_il.isoformat() if l.creato_il else ""}
            for l in db.query(models.Log).order_by(models.Log.creato_il.desc()).limit(limit).all()]

# ── STATISTICHE ────────────────────────────────────────────────
@app.get("/api/statistiche/categorie")
def stat_categorie(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    from sqlalchemy import func
    return [{"categoria": r.categoria1 or "Non classificato", "totale": r.totale}
            for r in db.query(models.Prodotto.categoria1,
                              func.count(models.Prodotto.id).label("totale"))
            .group_by(models.Prodotto.categoria1)
            .order_by(func.count(models.Prodotto.id).desc()).all()]

# ── ROOT ───────────────────────────────────────────────────────
@app.get("/", response_class=HTMLResponse)
def root():
    index_path = os.path.join(static_dir, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return HTMLResponse("<h1>BindManager Pro</h1>")
