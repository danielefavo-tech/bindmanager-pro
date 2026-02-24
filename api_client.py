"""
API CLIENT per programmi esterni (CD, LP, Libri, ecc.)
Usare questo modulo nei programmi di catalogazione per inviare
i prodotti direttamente a BindManager Pro.

Esempio uso:
    from app.api_client import BindManagerClient
    client = BindManagerClient("https://bindmanager-pro-production.up.railway.app", "admin@bindmanager.it", "bindmanager2024")
    client.crea_prodotto({
        "codice": "12345",
        "titolo": "Pink Floyd - The Wall",
        "categoria1": "Dischi vinile 33 giri",
        ...
    })
"""
import requests
import logging
logger = logging.getLogger(__name__)

class BindManagerClient:
    def __init__(self, base_url: str, email: str, password: str):
        self.base_url = base_url.rstrip('/')
        self.token = None
        self._login(email, password)

    def _login(self, email, password):
        r = requests.post(f"{self.base_url}/api/auth/login",
                          data={"username": email, "password": password})
        r.raise_for_status()
        self.token = r.json()["access_token"]

    def _headers(self):
        return {"Authorization": f"Bearer {self.token}"}

    def crea_prodotto(self, dati: dict) -> dict:
        """
        Crea un nuovo prodotto. La quantità viene impostata a 1 automaticamente.
        Il prodotto è subito disponibile per BindCommerce.
        
        dati obbligatori: codice, titolo
        dati consigliati: ean, tipo_codice1, categoria1, stato_bene, prezzo_vendita,
                          autore, produttore, anno, foto1, tag, posizione_magazzino
        """
        r = requests.post(f"{self.base_url}/api/prodotti/crea",
                          json=dati, headers=self._headers())
        if r.status_code == 200:
            return r.json()
        else:
            logger.error(f"Errore creazione prodotto {dati.get('codice')}: {r.text}")
            return {"ok": False, "detail": r.text}

    def cerca_prodotto(self, codice: str) -> dict | None:
        """Cerca un prodotto per codice. Ritorna None se non trovato."""
        r = requests.get(f"{self.base_url}/api/prodotti",
                         params={"cerca": codice, "per_page": 5},
                         headers=self._headers())
        if r.status_code == 200:
            data = r.json()
            for p in data.get("prodotti", []):
                if p["codice"] == codice:
                    return p
        return None

    def genera_ai(self, prodotto_id: int) -> dict:
        """Genera descrizione AI per un prodotto esistente."""
        r = requests.post(f"{self.base_url}/api/prodotti/{prodotto_id}/genera-ai",
                          headers=self._headers())
        return r.json() if r.status_code == 200 else {"ok": False}
