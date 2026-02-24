"""
MODULO AI CLAUDE — BindManager Pro
Adattato da main_CD_CLAUDE.py di Daniele
"""
import json, re, time, logging
logger = logging.getLogger(__name__)
CLAUDE_MODEL = "claude-haiku-4-5-20251001"

def genera_descrizione_claude(artista, album, anno, label, generi, stili,
                               tracklist, paese, stato_fisico, specifiche, api_key) -> dict:
    try:
        import anthropic
    except ImportError:
        logger.error("Libreria anthropic non installata"); return {}
    if not api_key or not api_key.strip():
        return {}

    tracklist_testo = tracklist[:1000] if tracklist else "Non disponibile"
    stili_testo = stili if stili else generi
    cond_testo = f"{stato_fisico} — {specifiche}" if specifiche else stato_fisico
    anno_str = str(anno) if anno else ""
    decennio = ""
    if anno_str and len(anno_str) == 4:
        if anno_str[:3] == "197": decennio = "anni 70"
        elif anno_str[:3] == "198": decennio = "anni 80"
        elif anno_str[:3] == "199": decennio = "anni 90"
        elif anno_str[:3] == "200": decennio = "anni 2000"

    prompt = f"""Sei un critico musicale e copywriter esperto di musica per un negozio di dischi vintage italiano.
Scrivi una descrizione di vendita UNICA e ORIGINALE per questo prodotto.

DATI:
- Artista: {artista}
- Album/Titolo: {album}
- Anno: {anno_str} {f'({decennio})' if decennio else ''}
- Casa Discografica: {label}
- Generi: {generi}
- Stili: {stili_testo}
- Paese: {paese}
- Condizione: {cond_testo}
- Tracklist: {tracklist_testo}

REGOLE:
1. Descrizione UNICA per questo artista e disco
2. Usa conoscenze reali su {artista}
3. Cita almeno 2 brani dalla tracklist
4. Keyword SEO integrate naturalmente
5. Minimo 500 caratteri per ebay_description
6. Tutto in italiano

Rispondi SOLO con JSON valido senza markdown:
{{
  "ebay_description": "HTML con p,b,i,ul,li. Intestazione, contesto artista, stile album, brani evidenziati, condizione. MINIMO 500 caratteri.",
  "sito_description": "HTML narrativo poetico. Atmosfera, eredita musicale, valore collezionista. MINIMO 400 caratteri.",
  "tags_extra": ["tag1","tag2","tag3","tag4","tag5","tag6","tag7"]
}}"""

    try:
        client = anthropic.Anthropic(api_key=api_key.strip())
        message = client.messages.create(
            model=CLAUDE_MODEL, max_tokens=2400,
            messages=[{"role": "user", "content": prompt}]
        )
        raw = message.content[0].text.strip()
        raw = re.sub(r"^```(?:json)?\s*", "", raw)
        raw = re.sub(r"\s*```$", "", raw)
        return json.loads(raw)
    except json.JSONDecodeError as e:
        logger.warning(f"Claude JSON error: {e}"); return {}
    except Exception as e:
        err = str(e)
        if "rate_limit" in err.lower():
            time.sleep(30)
        logger.error(f"Claude error: {err[:100]}"); return {}


def genera_descrizione_libro(titolo, autore, anno, editore, stato, api_key) -> dict:
    try:
        import anthropic
    except ImportError:
        return {}
    if not api_key or not api_key.strip():
        return {}

    prompt = f"""Sei un libraio antiquario e copywriter esperto per un negozio italiano.
Scrivi una descrizione di vendita per questo libro usato.

DATI:
- Titolo: {titolo}
- Autore: {autore}
- Anno: {anno}
- Editore: {editore}
- Condizione: {stato}

Rispondi SOLO con JSON valido senza markdown:
{{
  "ebay_description": "HTML con p,b. Descrizione, contesto culturale, valore. MINIMO 400 caratteri.",
  "sito_description": "Testo narrativo. MINIMO 300 caratteri.",
  "tags_extra": ["tag1","tag2","tag3","tag4","tag5"]
}}"""

    try:
        client = anthropic.Anthropic(api_key=api_key.strip())
        message = client.messages.create(
            model=CLAUDE_MODEL, max_tokens=1800,
            messages=[{"role": "user", "content": prompt}]
        )
        raw = message.content[0].text.strip()
        raw = re.sub(r"^```(?:json)?\s*", "", raw)
        raw = re.sub(r"\s*```$", "", raw)
        return json.loads(raw)
    except Exception as e:
        logger.error(f"Claude libro error: {str(e)[:100]}"); return {}
