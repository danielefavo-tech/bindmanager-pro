"""
IMPORT EXCEL BIMAN → BindManager Pro
Mappa le 55 colonne del file Biman export verso il database interno
"""
import re
from typing import Optional

# ── INDICI COLONNE BIMAN (0-based) ─────────────────────────────
COL = {
    "codice":           0,
    "tipo_codice":      1,
    "seriale":          2,
    "cat_sconto":       3,
    "prz_acq_netto":    4,
    "prz_acq_netto_v":  5,
    "prz_vend_netto":   6,   # prezzo vendita IVA esclusa
    "prz_vend_netto_v": 7,
    "qt":               8,
    "iva":              9,
    "codice_iva":       10,
    "net_price1":       11,
    "net_price1_v":     12,
    "tipo":             13,
    "deposito":         14,
    "del":              15,
    "categoria1":       16,
    "categoria2":       17,
    "categoria3":       18,
    "categoria4":       19,
    "ean":              20,
    "spedizione":       21,
    "stato_bene":       22,
    "discogs":          23,
    "anno":             24,
    "rilegatura":       25,
    "tipo_prodotto":    26,
    "specifiche":       27,
    "binding":          28,
    "autore":           29,
    "tipo_codice1":     30,
    "codici_temp":      31,
    "dettaglio_stato":  32,
    "fornitore":        33,
    "codice_fornitore": 34,
    "produttore":       35,
    "mpn":              36,
    "posizione":        37,
    "descrizione_breve":38,
    "titolo":           39,
    "dettagli":         40,
    "descrizione":      41,
    "note":             42,
    "taglia":           43,
    "colore":           44,
    "cod_col_forn":     45,
    "colore1":          46,
    "taglia1":          47,
    "formato":          48,
    "sottoscorta":      49,
    "riordino_min":     50,
    "sottoscorta_eff":  51,
    "riordino_eff":     52,
    "tag":              53,
    "foto1":            54,
}


def _v(row, key) -> str:
    """Legge valore da riga per chiave colonna, ritorna stringa pulita."""
    try:
        idx = COL[key]
        val = row[idx]
        if val is None:
            return ""
        s = str(val).strip()
        return "" if s.lower() in ("none", "nan", "vuoto", "n/a") else s
    except (IndexError, KeyError):
        return ""


def _float(row, key) -> float:
    """Legge valore float, ritorna 0.0 se non valido."""
    try:
        s = _v(row, key)
        return float(s) if s else 0.0
    except ValueError:
        return 0.0


def _int(row, key) -> int:
    """Legge valore int (quantità), ritorna 0 se non valido."""
    try:
        s = _v(row, key)
        f = float(s) if s else 0.0
        return int(f)
    except ValueError:
        return 0


def estrai_categoria_da_titolo(titolo: str) -> tuple:
    """
    Estrae la categoria dal titolo se presente tra parentesi.
    Es: 'Alfried Krupp (Libri e Riviste)' → ('Libri e Riviste', '')
    """
    if not titolo:
        return ("", "")
    match = re.search(r'\(([^)]+)\)\s*$', titolo)
    if match:
        cat = match.group(1).strip()
        return (cat, "")
    return ("", "")


def calcola_prezzo_ivato(prezzo_netto: float, iva_str: str) -> float:
    """Calcola prezzo IVA inclusa."""
    try:
        iva = float(iva_str) if iva_str else 0.0
        # Se IVA è già decimale (0.10) la moltiplico, se è percentuale (10) la divido
        if iva > 1:
            iva = iva / 100
        return round(prezzo_netto * (1 + iva), 2)
    except Exception:
        return prezzo_netto


def row_to_prodotto(row) -> Optional[dict]:
    """
    Converte una riga Excel Biman in dict prodotto per il database.
    Ritorna None se la riga è vuota/invalida.
    """
    codice = _v(row, "codice")
    titolo = _v(row, "titolo")

    if not codice and not titolo:
        return None

    # Categoria: prima dal campo, poi estratta dal titolo
    cat1 = _v(row, "categoria1")
    cat2 = _v(row, "categoria2")
    if not cat1:
        cat1, cat2 = estrai_categoria_da_titolo(titolo)

    # Prezzo: usa prezzo netto e calcola ivato
    prz_netto = _float(row, "prz_vend_netto")
    iva_str = _v(row, "iva")
    prz_ivato = calcola_prezzo_ivato(prz_netto, iva_str)

    # Titolo pulito (rimuovi categoria tra parentesi finale)
    titolo_pulito = re.sub(r'\s*\([^)]+\)\s*$', '', titolo).strip()

    return {
        "codice":           codice,
        "ean":              _v(row, "ean"),
        "titolo":           titolo_pulito or titolo,
        "autore":           _v(row, "autore") or _v(row, "produttore"),
        "anno":             _v(row, "anno"),
        "categoria1":       cat1,
        "categoria2":       cat2,
        "categoria3":       _v(row, "categoria3"),
        "categoria4":       _v(row, "categoria4"),
        "tipo_prodotto":    _v(row, "tipo_prodotto") or _v(row, "tipo"),
        "produttore":       _v(row, "produttore"),
        "stato_bene":       _v(row, "stato_bene"),
        "specifiche":       _v(row, "specifiche"),
        "dettaglio_stato":  _v(row, "dettaglio_stato"),
        "prezzo_acquisto":  0.0,
        "prezzo_vendita":   prz_ivato,
        "quantita":         _int(row, "qt"),
        "posizione_magazzino": _v(row, "posizione"),
        "descrizione_breve": _v(row, "descrizione_breve"),
        "descrizione":      _v(row, "descrizione"),
        "note":             _v(row, "note"),
        "tag":              _v(row, "tag"),
        "foto1":            _v(row, "foto1"),
        "foto2":            "",
        "foto3":            "",
        "ai_generata":      False,
        "bindcommerce_inviato": False,
    }


def valida_riga(prodotto: dict) -> list:
    """Ritorna lista di warning per una riga. Lista vuota = OK."""
    warnings = []
    if not prodotto.get("codice"):
        warnings.append("Codice mancante")
    if not prodotto.get("titolo"):
        warnings.append("Titolo mancante")
    if not prodotto.get("ean"):
        warnings.append("EAN mancante")
    if prodotto.get("prezzo_vendita", 0) <= 0:
        warnings.append("Prezzo non valido")
    if prodotto.get("quantita", 0) < 0:
        warnings.append("Quantità negativa")
    return warnings
