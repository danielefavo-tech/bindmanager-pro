# BindManager Pro — Deploy su Railway

## Struttura progetto
```
bindmanager/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI backend
│   ├── models.py            # Database SQLAlchemy
│   ├── database.py          # Connessione DB
│   ├── auth.py              # JWT autenticazione
│   ├── ai_claude.py         # Modulo AI Claude
│   ├── import_excel.py      # Import file Biman
│   └── categorie_mapping.py # Mappatura categorie BC
├── static/
│   └── index.html           # Frontend pannello
├── requirements.txt
├── Procfile
└── railway.json
```

## Deploy Railway (5 minuti)

### 1. Crea account GitHub
Vai su github.com → Sign Up (gratuito)

### 2. Crea repository GitHub
- New repository → Nome: `bindmanager-pro`
- Carica tutti i file di questa cartella

### 3. Crea account Railway
Vai su railway.app → Login con GitHub

### 4. Nuovo progetto Railway
- New Project → Deploy from GitHub repo
- Seleziona `bindmanager-pro`
- Railway installa tutto automaticamente

### 5. Aggiungi PostgreSQL
- Nel progetto Railway → New → Database → PostgreSQL
- Railway collegherà automaticamente il DATABASE_URL

### 6. Variabili d'ambiente da impostare
Nel pannello Railway → Variables:
```
SECRET_KEY=cambia-questa-chiave-con-qualcosa-di-sicuro-2024
```

### 7. Deploy completato!
Railway genera URL tipo: `https://bindmanager-pro-production.up.railway.app`

## Primo accesso
- Email: `admin@bindmanager.it`
- Password: `bindmanager2024`

⚠️ IMPORTANTE: Cambia la password dal pannello dopo il primo accesso!

## Configurazione API Keys (dal pannello → Impostazioni)
1. **Claude API Key**: console.anthropic.com → API Keys
2. **BindCommerce API Key**: pannello BindCommerce → Impostazioni → API

## Import prodotti
1. Esporta da Biman il file WIDE (tutti i 55 campi)
2. Vai su Import Excel nel pannello
3. Carica il file → Avvia Import
4. (Opzionale) Attiva "Genera descrizioni AI" per generare le descrizioni automaticamente

## Costi stimati mensili
| Servizio | Costo |
|----------|-------|
| Railway (app + DB) | ~$5/mese |
| Claude API (28.000 prodotti) | ~$28 una tantum, poi $0.001/nuovo |
| Totale regime | ~$5-8/mese |
