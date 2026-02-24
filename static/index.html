<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BindManager Pro</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Inter:wght@300;400;500;600;700&display=swap');

:root {
  --bg:       #f0f2f5;
  --bg2:      #ffffff;
  --bg3:      #f7f8fa;
  --border:   #e2e6ea;
  --border2:  #d0d5dd;
  --text:     #1a202c;
  --text2:    #4a5568;
  --text3:    #9aa5b4;
  --accent:   #2563eb;
  --accent2:  #1d4ed8;
  --green:    #059669;
  --red:      #dc2626;
  --orange:   #d97706;
  --purple:   #7c3aed;
  --mono:     'JetBrains Mono', monospace;
  --sans:     'Inter', sans-serif;
  --radius:   8px;
  --shadow:   0 2px 12px rgba(0,0,0,0.08);
}

* { box-sizing: border-box; margin: 0; padding: 0; }
html,body { height: 100%; background: var(--bg); color: var(--text); font-family: var(--sans); font-size: 14px; }

/* ── LAYOUT ── */
#app { display: flex; height: 100vh; overflow: hidden; }
#sidebar { width: 220px; min-width: 220px; background: #1e293b; border-right: 1px solid #1e293b; display: flex; flex-direction: column; }
#main { flex: 1; display: flex; flex-direction: column; overflow: hidden; }
#topbar { height: 54px; background: var(--bg2); border-bottom: 1px solid var(--border); display: flex; align-items: center; padding: 0 20px; gap: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.06); }
#content { flex: 1; overflow-y: auto; padding: 24px; }

/* ── SIDEBAR ── */
.sidebar-logo { padding: 18px 16px 14px; border-bottom: 1px solid rgba(255,255,255,0.1); }
.sidebar-logo h1 { font-size: 15px; font-weight: 700; color: #ffffff; letter-spacing: 0.5px; }
.sidebar-logo span { font-family: var(--mono); font-size: 10px; color: #60a5fa; display: block; margin-top: 2px; }
.sidebar-nav { flex: 1; padding: 10px 0; overflow-y: auto; }
.nav-item { display: flex; align-items: center; gap: 10px; padding: 9px 16px; cursor: pointer; color: #94a3b8; font-size: 13px; font-weight: 500; border-left: 3px solid transparent; transition: all 0.15s; user-select: none; }
.nav-item:hover { background: rgba(255,255,255,0.05); color: #ffffff; }
.nav-item.active { background: rgba(96,165,250,0.15); color: #60a5fa; border-left-color: #60a5fa; }
.nav-item .icon { font-size: 16px; width: 20px; text-align: center; }
.nav-section { padding: 14px 16px 4px; font-size: 10px; font-weight: 600; color: #475569; text-transform: uppercase; letter-spacing: 1px; }
.sidebar-footer { padding: 12px 16px; border-top: 1px solid rgba(255,255,255,0.1); font-size: 12px; color: #64748b; }
.sidebar-footer strong { color: #cbd5e1; display: block; }

/* ── TOPBAR ── */
.topbar-title { font-size: 15px; font-weight: 600; flex: 1; }
.topbar-badge { background: var(--bg3); border: 1px solid var(--border2); border-radius: 20px; padding: 3px 10px; font-size: 11px; color: var(--text2); font-family: var(--mono); }

/* ── CARDS ── */
.stat-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 14px; margin-bottom: 24px; }
.stat-card { background: var(--bg2); border: 1px solid var(--border); border-radius: var(--radius); padding: 16px 18px; }
.stat-card .label { font-size: 11px; color: var(--text3); text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 6px; }
.stat-card .value { font-size: 26px; font-weight: 700; font-family: var(--mono); }
.stat-card .value.green { color: var(--green); }
.stat-card .value.red { color: var(--red); }
.stat-card .value.orange { color: var(--orange); }
.stat-card .value.blue { color: var(--accent); }
.stat-card .value.purple { color: var(--purple); }

/* ── PANELS ── */
.panel { background: var(--bg2); border: 1px solid var(--border); border-radius: var(--radius); margin-bottom: 20px; }
.panel-header { padding: 14px 18px; border-bottom: 1px solid var(--border); display: flex; align-items: center; justify-content: space-between; }
.panel-header h3 { font-size: 13px; font-weight: 600; }
.panel-body { padding: 16px 18px; }

/* ── BUTTONS ── */
.btn { display: inline-flex; align-items: center; gap: 6px; padding: 7px 14px; border-radius: 6px; border: none; cursor: pointer; font-size: 13px; font-weight: 500; transition: all 0.15s; font-family: var(--sans); }
.btn-primary { background: var(--accent); color: #fff; }
.btn-primary:hover { background: var(--accent2); }
.btn-success { background: var(--green); color: #fff; }
.btn-success:hover { background: #059669; }
.btn-danger { background: var(--red); color: #fff; }
.btn-danger:hover { background: #dc2626; }
.btn-ghost { background: var(--bg3); color: var(--text2); border: 1px solid var(--border2); }
.btn-ghost:hover { color: var(--text); border-color: var(--text3); }
.btn-sm { padding: 4px 10px; font-size: 12px; }
.btn:disabled { opacity: 0.5; cursor: not-allowed; }

/* ── FORM ── */
.form-group { margin-bottom: 14px; }
.form-label { display: block; font-size: 12px; color: var(--text2); margin-bottom: 5px; font-weight: 500; }
.form-input, .form-select, .form-textarea {
  width: 100%; background: var(--bg3); border: 1px solid var(--border2);
  border-radius: 6px; padding: 8px 10px; color: var(--text); font-size: 13px;
  font-family: var(--sans); transition: border-color 0.15s;
}
.form-input:focus, .form-select:focus, .form-textarea:focus {
  outline: none; border-color: var(--accent);
}
.form-textarea { resize: vertical; min-height: 80px; }
.form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
.form-row-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 14px; }

/* ── TABLE ── */
.table-wrap { overflow-x: auto; }
table { width: 100%; border-collapse: collapse; }
th { background: var(--bg3); padding: 9px 12px; text-align: left; font-size: 11px; font-weight: 600; color: var(--text3); text-transform: uppercase; letter-spacing: 0.6px; border-bottom: 1px solid var(--border); white-space: nowrap; }
td { padding: 9px 12px; border-bottom: 1px solid var(--border); font-size: 13px; vertical-align: middle; }
tr:hover td { background: var(--bg3); }
.td-code { font-family: var(--mono); font-size: 12px; color: var(--accent); }
.td-title { max-width: 280px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.td-img { width: 40px; height: 40px; object-fit: cover; border-radius: 4px; background: var(--bg3); }
.td-img-ph { width: 40px; height: 40px; background: var(--bg3); border-radius: 4px; display: flex; align-items: center; justify-content: center; color: var(--text3); font-size: 18px; }

/* ── BADGES ── */
.badge { display: inline-block; padding: 2px 8px; border-radius: 12px; font-size: 11px; font-weight: 600; }
.badge-green { background: rgba(16,185,129,0.15); color: var(--green); }
.badge-red { background: rgba(239,68,68,0.15); color: var(--red); }
.badge-orange { background: rgba(245,158,11,0.15); color: var(--orange); }
.badge-blue { background: rgba(59,130,246,0.15); color: var(--accent); }
.badge-purple { background: rgba(139,92,246,0.15); color: var(--purple); }
.badge-gray { background: var(--bg3); color: var(--text3); }

/* ── SEARCH BAR ── */
.search-bar { display: flex; gap: 10px; margin-bottom: 16px; flex-wrap: wrap; }
.search-bar .form-input { max-width: 300px; }
.search-bar .form-select { max-width: 160px; }

/* ── UPLOAD AREA ── */
.upload-area { border: 2px dashed var(--border2); border-radius: var(--radius); padding: 32px; text-align: center; cursor: pointer; transition: all 0.2s; }
.upload-area:hover, .upload-area.drag { border-color: var(--accent); background: rgba(59,130,246,0.05); }
.upload-area .icon { font-size: 36px; margin-bottom: 10px; }
.upload-area p { color: var(--text2); font-size: 13px; }
.upload-area strong { color: var(--accent); }

/* ── LOG LIST ── */
.log-list { max-height: 320px; overflow-y: auto; }
.log-item { display: flex; gap: 10px; padding: 7px 0; border-bottom: 1px solid var(--border); font-size: 12px; }
.log-item:last-child { border-bottom: none; }
.log-time { color: var(--text3); font-family: var(--mono); white-space: nowrap; min-width: 80px; }
.log-op { font-weight: 600; min-width: 120px; }
.log-detail { color: var(--text2); flex: 1; }
.log-item.success .log-op { color: var(--green); }
.log-item.error .log-op { color: var(--red); }
.log-item.warning .log-op { color: var(--orange); }
.log-item.info .log-op { color: var(--accent); }

/* ── MODAL ── */
.modal-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.7); z-index: 1000; display: flex; align-items: center; justify-content: center; padding: 20px; }
.modal { background: var(--bg2); border: 1px solid var(--border2); border-radius: 10px; max-width: 680px; width: 100%; max-height: 85vh; overflow-y: auto; box-shadow: var(--shadow); }
.modal-header { padding: 18px 20px 14px; border-bottom: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center; }
.modal-header h3 { font-size: 15px; font-weight: 600; }
.modal-body { padding: 20px; }
.modal-footer { padding: 14px 20px; border-top: 1px solid var(--border); display: flex; justify-content: flex-end; gap: 10px; }
.btn-close { background: none; border: none; color: var(--text3); cursor: pointer; font-size: 20px; line-height: 1; padding: 2px; }
.btn-close:hover { color: var(--text); }

/* ── PROGRESS ── */
.progress-bar { height: 4px; background: var(--border); border-radius: 2px; overflow: hidden; margin-top: 10px; }
.progress-fill { height: 100%; background: var(--accent); border-radius: 2px; transition: width 0.3s; }

/* ── ALERTS ── */
.alert { padding: 10px 14px; border-radius: 6px; font-size: 13px; margin-bottom: 14px; display: flex; gap: 8px; align-items: flex-start; }
.alert-success { background: rgba(16,185,129,0.1); border: 1px solid rgba(16,185,129,0.3); color: var(--green); }
.alert-error { background: rgba(239,68,68,0.1); border: 1px solid rgba(239,68,68,0.3); color: var(--red); }
.alert-info { background: rgba(59,130,246,0.1); border: 1px solid rgba(59,130,246,0.3); color: var(--accent); }

/* ── PAGINATION ── */
.pagination { display: flex; align-items: center; gap: 8px; margin-top: 16px; justify-content: center; }
.page-btn { padding: 5px 10px; border-radius: 5px; border: 1px solid var(--border2); background: var(--bg3); color: var(--text2); cursor: pointer; font-size: 12px; }
.page-btn.active { background: var(--accent); color: #fff; border-color: var(--accent); }
.page-btn:hover:not(.active) { color: var(--text); }
.page-info { font-size: 12px; color: var(--text3); }

/* ── EMPTY STATE ── */
.empty-state { text-align: center; padding: 48px 20px; }
.empty-state .icon { font-size: 48px; margin-bottom: 12px; opacity: 0.3; }
.empty-state p { color: var(--text3); }

/* ── VIEWS ── */
.view { display: none; }
.view.active { display: block; }

/* ── DESCRIPTION PREVIEW ── */
.desc-preview { background: var(--bg3); border: 1px solid var(--border); border-radius: 6px; padding: 12px; max-height: 200px; overflow-y: auto; font-size: 12px; color: var(--text2); line-height: 1.6; }

/* ── SCROLL ── */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--border2); border-radius: 3px; }
</style>
</head>
<body>

<!-- LOGIN -->
<div id="login-screen" style="display:flex;align-items:center;justify-content:center;height:100vh;background:linear-gradient(135deg,#f0f4ff 0%,#e8f0fe 100%);">
  <div style="background:#ffffff;border:1px solid var(--border);border-radius:12px;padding:36px;width:340px;box-shadow:0 8px 32px rgba(37,99,235,0.1);">
    <div style="text-align:center;margin-bottom:28px;">
      <div style="font-size:36px;margin-bottom:8px;">📦</div>
      <h2 style="font-size:20px;font-weight:700;color:#1a202c;">BindManager Pro</h2>
      <p style="color:var(--text3);font-size:12px;margin-top:4px;">Pannello di gestione catalogo</p>
    </div>
    <div id="login-error" class="alert alert-error" style="display:none;"></div>
    <div class="form-group">
      <label class="form-label">Email</label>
      <input id="login-email" class="form-input" type="email" value="admin@bindmanager.it" placeholder="email@esempio.it">
    </div>
    <div class="form-group">
      <label class="form-label">Password</label>
      <input id="login-password" class="form-input" type="password" value="bindmanager2024" placeholder="••••••••">
    </div>
    <button class="btn btn-primary" style="width:100%;justify-content:center;margin-top:8px;" onclick="doLogin()">
      Accedi →
    </button>
  </div>
</div>

<!-- APP -->
<div id="app" style="display:none;">

  <!-- SIDEBAR -->
  <div id="sidebar">
    <div class="sidebar-logo">
      <h1>📦 BindManager</h1>
      <span>PRO v1.0</span>
    </div>
    <nav class="sidebar-nav">
      <div class="nav-section">Principale</div>
      <div class="nav-item active" onclick="showView('dashboard')">
        <span class="icon">⚡</span> Dashboard
      </div>
      <div class="nav-item" onclick="showView('prodotti')">
        <span class="icon">📋</span> Catalogo
      </div>
      <div class="nav-section">Operazioni</div>
      <div class="nav-item" onclick="showView('import')">
        <span class="icon">⬆️</span> Import Excel
      </div>
      <div class="nav-item" onclick="showView('ai')">
        <span class="icon">🤖</span> AI Descrizioni
      </div>
      <div class="nav-section">Sistema</div>
      <div class="nav-item" onclick="showView('logs')">
        <span class="icon">📜</span> Log Operazioni
      </div>
      <div class="nav-item" id="nav-impostazioni" onclick="showView('impostazioni')" style="display:none;">
        <span class="icon">⚙️</span> Impostazioni
      </div>
      <div class="nav-item" id="nav-utenti" onclick="showView('utenti')" style="display:none;">
        <span class="icon">👥</span> Utenti
      </div>
    </nav>
    <div class="sidebar-footer">
      <strong id="user-nome">—</strong>
      <span id="user-email" style="font-size:11px;"></span>
      <div style="margin-top:6px;">
        <span id="user-badge" class="badge badge-blue" style="font-size:10px;background:rgba(96,165,250,0.2);color:#60a5fa;"></span>
        &nbsp;
        <a href="#" onclick="doLogout()" style="font-size:11px;color:var(--text3);text-decoration:none;">Esci</a>
      </div>
    </div>
  </div>

  <!-- MAIN -->
  <div id="main">
    <div id="topbar">
      <span class="topbar-title" id="topbar-title">Dashboard</span>
      <span class="topbar-badge" id="topbar-count">—</span>
    </div>

    <div id="content">

      <!-- ═══ DASHBOARD ═══ -->
      <div id="view-dashboard" class="view active">
        <div class="stat-grid" id="stat-grid">
          <div class="stat-card"><div class="label">Totale Prodotti</div><div class="value blue" id="s-totale">—</div></div>
          <div class="stat-card"><div class="label">Con Foto</div><div class="value green" id="s-foto">—</div></div>
          <div class="stat-card"><div class="label">Descrizioni AI</div><div class="value purple" id="s-ai">—</div></div>
          <div class="stat-card"><div class="label">Inviati BC</div><div class="value blue" id="s-bc">—</div></div>
          <div class="stat-card"><div class="label">Esauriti</div><div class="value red" id="s-esauriti">—</div></div>
          <div class="stat-card"><div class="label">Sottoscorta</div><div class="value orange" id="s-sotto">—</div></div>
        </div>

        <div class="panel">
          <div class="panel-header">
            <h3>📜 Ultime Operazioni</h3>
            <button class="btn btn-ghost btn-sm" onclick="loadDashboard()">↻ Aggiorna</button>
          </div>
          <div class="panel-body">
            <div class="log-list" id="dash-logs"><div class="empty-state"><p>Nessuna operazione registrata</p></div></div>
          </div>
        </div>

        <div class="panel">
          <div class="panel-header"><h3>📊 Distribuzione Categorie</h3></div>
          <div class="panel-body" id="cat-chart" style="display:flex;flex-wrap:wrap;gap:8px;"></div>
        </div>
      </div>

      <!-- ═══ PRODOTTI ═══ -->
      <div id="view-prodotti" class="view">
        <div class="search-bar">
          <input id="search-input" class="form-input" placeholder="🔍 Cerca codice, titolo, EAN, autore..." oninput="searchDebounce()">
          <select id="filter-cat" class="form-select" onchange="loadProdotti(1)">
            <option value="">Tutte le categorie</option>
            <option>Cd</option>
            <option>Dischi vinile 33 giri</option>
            <option>Dischi Vinile 45 giri</option>
            <option>Film e DVD</option>
            <option>Libri e Riviste</option>
            <option>Musicassette</option>
          </select>
          <select id="filter-stato" class="form-select" onchange="loadProdotti(1)">
            <option value="">Tutti gli stati</option>
            <option>Nuovo</option>
            <option>Sigillato</option>
            <option>Come nuovo</option>
            <option>Ottime condizioni</option>
            <option>Buone condizioni</option>
            <option>Condizioni accettabili</option>
            <option>Usato</option>
          </select>
          <label style="display:flex;align-items:center;gap:6px;color:var(--text2);font-size:12px;cursor:pointer;">
            <input type="checkbox" id="filter-esauriti" onchange="loadProdotti(1)"> Solo esauriti
          </label>
          <label style="display:flex;align-items:center;gap:6px;color:var(--text2);font-size:12px;cursor:pointer;">
            <input type="checkbox" id="filter-noai" onchange="loadProdotti(1)"> Senza AI
          </label>
        </div>

        <div class="panel">
          <div class="panel-header">
            <h3>📋 Catalogo Prodotti</h3>
            <span id="prodotti-count" class="badge badge-blue">—</span>
          </div>
          <div class="panel-body" style="padding:0;">
            <div class="table-wrap">
              <table>
                <thead>
                  <tr>
                    <th>Foto</th>
                    <th>Codice</th>
                    <th>Titolo</th>
                    <th>Categoria</th>
                    <th>Stato</th>
                    <th>Prezzo</th>
                    <th>Qt</th>
                    <th>AI</th>
                    <th></th>
                  </tr>
                </thead>
                <tbody id="prodotti-tbody">
                  <tr><td colspan="9" style="text-align:center;padding:32px;color:var(--text3);">Caricamento...</td></tr>
                </tbody>
              </table>
            </div>
            <div style="padding:12px 18px;">
              <div class="pagination" id="pagination"></div>
            </div>
          </div>
        </div>
      </div>

      <!-- ═══ IMPORT ═══ -->
      <div id="view-import" class="view">
        <div class="panel">
          <div class="panel-header"><h3>⬆️ Import File Excel Biman</h3></div>
          <div class="panel-body">
            <div class="alert alert-info">
              📌 Carica il file Excel esportato da Biman (formato WIDE). Vengono importati tutti i 55 campi, le categorie vengono mappate automaticamente verso BindCommerce.
            </div>

            <div class="upload-area" id="upload-area" onclick="document.getElementById('file-input').click()"
                 ondragover="event.preventDefault();this.classList.add('drag')"
                 ondragleave="this.classList.remove('drag')"
                 ondrop="handleDrop(event)">
              <div class="icon">📊</div>
              <p>Trascina il file Excel qui oppure <strong>clicca per selezionare</strong></p>
              <p style="margin-top:6px;font-size:12px;color:var(--text3);">Supporta .xlsx — Biman Export Wide</p>
              <input id="file-input" type="file" accept=".xlsx" style="display:none" onchange="handleFileSelect(event)">
            </div>

            <div id="file-selected" style="display:none;margin-top:14px;">
              <div class="alert alert-success">
                ✅ File selezionato: <strong id="file-name">—</strong>
              </div>
            </div>

            <div style="margin-top:16px;" class="form-row">
              <div>
                <label class="form-label">Modalità Import</label>
                <select id="opt-modalita" class="form-select">
                  <option value="entrambi">Nuovi + Aggiorna esistenti</option>
                  <option value="nuovi">Solo nuovi prodotti</option>
                  <option value="aggiorna">Solo aggiorna esistenti</option>
                </select>
              </div>
            </div>

            <div style="margin-top:18px;">
              <button class="btn btn-primary" id="btn-import" onclick="doImport()" disabled>
                ⬆️ Avvia Import
              </button>
            </div>

            <div id="import-progress" style="display:none;margin-top:16px;">
              <div style="color:var(--text2);font-size:13px;" id="import-status">Importazione in corso...</div>
              <div class="progress-bar"><div class="progress-fill" id="progress-fill" style="width:0%"></div></div>
            </div>

            <div id="import-result" style="display:none;margin-top:16px;"></div>
          </div>
        </div>

        <div class="panel">
          <div class="panel-header"><h3>ℹ️ Mappatura Colonne Biman → BindManager</h3></div>
          <div class="panel-body">
            <div class="table-wrap">
              <table>
                <thead><tr><th>Colonna Biman</th><th>Campo BindManager</th><th>Note</th></tr></thead>
                <tbody>
                  <tr><td class="td-code">Codice</td><td>SKU prodotto</td><td>Identificatore univoco</td></tr>
                  <tr><td class="td-code">Codice a barre</td><td>EAN / Barcode</td><td>Usato per matching foto</td></tr>
                  <tr><td class="td-code">Titolo</td><td>Titolo prodotto</td><td>Pulito dalla categoria tra ()</td></tr>
                  <tr><td class="td-code">AUTORE / Produttore</td><td>Autore / Artista</td><td>Per descrizione AI</td></tr>
                  <tr><td class="td-code">Categoria 1 / 2</td><td>Categoria BindCommerce</td><td>Mappatura automatica</td></tr>
                  <tr><td class="td-code">prz Vend. IVA esclusa</td><td>Prezzo vendita</td><td>IVA calcolata automaticamente</td></tr>
                  <tr><td class="td-code">Qt</td><td>Quantità stock</td><td>—</td></tr>
                  <tr><td class="td-code">Stato del bene</td><td>Condizione</td><td>Come nuovo, Buone condizioni...</td></tr>
                  <tr><td class="td-code">Posizione magazzino</td><td>Posizione</td><td>—</td></tr>
                  <tr><td class="td-code">Descrizione</td><td>Descrizione eBay</td><td>Sostituita da AI se vuota</td></tr>
                  <tr><td class="td-code">foto 1</td><td>URL Foto 1</td><td>URL già presente da BindCommerce</td></tr>
                  <tr><td class="td-code">Tag</td><td>Tag prodotto</td><td>Estesi da AI</td></tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>

      <!-- ═══ AI ═══ -->
      <div id="view-ai" class="view">
        <div class="panel">
          <div class="panel-header"><h3>🤖 Generazione Descrizioni AI</h3></div>
          <div class="panel-body">
            <div class="alert alert-info">
              🤖 Usa Claude Haiku per generare descrizioni professionali per ogni prodotto. Costo stimato: ~€0.001 per prodotto. Il modulo AI è quello già calibrato dal tuo programma Python.
            </div>

            <div class="form-row" style="margin-bottom:16px;">
              <div>
                <label class="form-label">Prodotti senza descrizione AI</label>
                <div style="font-size:24px;font-weight:700;font-family:var(--mono);color:var(--orange);" id="ai-count-missing">—</div>
              </div>
              <div>
                <label class="form-label">Già con descrizione AI</label>
                <div style="font-size:24px;font-weight:700;font-family:var(--mono);color:var(--green);" id="ai-count-done">—</div>
              </div>
            </div>

            <div class="form-group">
              <label class="form-label">Filtra per categoria</label>
              <select id="ai-cat-filter" class="form-select" style="max-width:260px;">
                <option value="">Tutte le categorie</option>
                <option>Cd</option>
                <option>Dischi vinile 33 giri</option>
                <option>Dischi Vinile 45 giri</option>
                <option>Film e DVD</option>
                <option>Libri e Riviste</option>
              </select>
            </div>

            <div class="form-group">
              <label class="form-label">Limite prodotti per questa sessione</label>
              <input id="ai-limit" class="form-input" type="number" value="50" min="1" max="1000" style="max-width:120px;">
              <p style="font-size:11px;color:var(--text3);margin-top:4px;">Costo stimato: <span id="ai-cost">€0.05</span></p>
            </div>

            <button class="btn btn-primary" id="btn-genera-ai" onclick="generaAIBatch()">
              🤖 Genera Descrizioni AI
            </button>

            <div id="ai-progress" style="display:none;margin-top:16px;">
              <div style="color:var(--text2);font-size:13px;" id="ai-status">Generazione in corso...</div>
              <div class="progress-bar"><div class="progress-fill" id="ai-progress-fill" style="width:0%"></div></div>
              <div style="font-size:12px;color:var(--text3);margin-top:6px;" id="ai-counter">0 / 0</div>
            </div>
          </div>
        </div>
      </div>

      <!-- ═══ LOGS ═══ -->
      <div id="view-logs" class="view">
        <div class="panel">
          <div class="panel-header">
            <h3>📜 Log Operazioni</h3>
            <button class="btn btn-ghost btn-sm" onclick="loadLogs()">↻ Aggiorna</button>
          </div>
          <div class="panel-body" style="padding:0;">
            <div class="table-wrap">
              <table>
                <thead><tr><th>Data/Ora</th><th>Operazione</th><th>Dettaglio</th><th>Utente</th></tr></thead>
                <tbody id="logs-tbody">
                  <tr><td colspan="4" style="text-align:center;padding:32px;color:var(--text3);">Caricamento...</td></tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>

      <!-- ═══ IMPOSTAZIONI ═══ -->
      <div id="view-impostazioni" class="view">
        <div class="panel">
          <div class="panel-header"><h3>⚙️ Configurazione API</h3></div>
          <div class="panel-body">
            <div id="config-alert"></div>
            <div class="form-group">
              <label class="form-label">🤖 API Key Claude (Anthropic)</label>
              <div style="display:flex;gap:8px;">
                <input id="cfg-claude" class="form-input" type="password" placeholder="sk-ant-...">
                <button class="btn btn-primary" onclick="saveConfig('claude_api_key', 'cfg-claude')">Salva</button>
              </div>
              <p style="font-size:11px;color:var(--text3);margin-top:4px;">Recupera da: console.anthropic.com → API Keys</p>
            </div>
            <div class="form-group">
              <label class="form-label">🔗 API Key BindCommerce</label>
              <div style="display:flex;gap:8px;">
                <input id="cfg-bc" class="form-input" type="password" placeholder="La tua API key BindCommerce">
                <button class="btn btn-primary" onclick="saveConfig('bindcommerce_api_key', 'cfg-bc')">Salva</button>
              </div>
            </div>
            <div class="form-group">
              <label class="form-label">🕐 Intervallo Sync Magazzino</label>
              <div style="display:flex;gap:8px;align-items:center;">
                <select id="cfg-sync" class="form-select" style="max-width:160px;">
                  <option value="15">Ogni 15 minuti</option>
                  <option value="30" selected>Ogni 30 minuti</option>
                  <option value="60">Ogni 60 minuti</option>
                </select>
                <button class="btn btn-primary" onclick="saveConfig('sync_interval', 'cfg-sync')">Salva</button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- ═══ UTENTI ═══ -->
      <div id="view-utenti" class="view">
        <div class="panel">
          <div class="panel-header">
            <h3>👥 Gestione Utenti</h3>
            <button class="btn btn-success btn-sm" onclick="openNewUser()">+ Nuovo Utente</button>
          </div>
          <div class="panel-body" style="padding:0;">
            <div class="table-wrap">
              <table>
                <thead><tr><th>Nome</th><th>Email</th><th>Ruolo</th><th>Stato</th><th></th></tr></thead>
                <tbody id="utenti-tbody"><tr><td colspan="5" style="text-align:center;padding:24px;color:var(--text3);">Caricamento...</td></tr></tbody>
              </table>
            </div>
          </div>
        </div>
      </div>

    </div><!-- /content -->
  </div><!-- /main -->
</div><!-- /app -->

<!-- MODAL PRODOTTO -->
<div id="modal-prodotto" class="modal-overlay" style="display:none;" onclick="if(event.target===this)closeModal('modal-prodotto')">
  <div class="modal">
    <div class="modal-header">
      <h3 id="modal-prodotto-title">Dettaglio Prodotto</h3>
      <button class="btn-close" onclick="closeModal('modal-prodotto')">×</button>
    </div>
    <div class="modal-body" id="modal-prodotto-body">
    </div>
    <div class="modal-footer">
      <button class="btn btn-ghost" onclick="closeModal('modal-prodotto')">Chiudi</button>
      <button class="btn btn-primary" id="btn-rigenera-ai" onclick="rigeneraAI()">🤖 Rigenera AI</button>
    </div>
  </div>
</div>

<!-- MODAL NUOVO UTENTE -->
<div id="modal-nuovo-utente" class="modal-overlay" style="display:none;" onclick="if(event.target===this)closeModal('modal-nuovo-utente')">
  <div class="modal" style="max-width:400px;">
    <div class="modal-header">
      <h3>Nuovo Utente</h3>
      <button class="btn-close" onclick="closeModal('modal-nuovo-utente')">×</button>
    </div>
    <div class="modal-body">
      <div class="form-group"><label class="form-label">Nome</label><input id="new-nome" class="form-input"></div>
      <div class="form-group"><label class="form-label">Email</label><input id="new-email" class="form-input" type="email"></div>
      <div class="form-group"><label class="form-label">Password</label><input id="new-password" class="form-input" type="password"></div>
      <div class="form-group">
        <label class="form-label">Ruolo</label>
        <select id="new-ruolo" class="form-select">
          <option value="collaboratore">Collaboratore</option>
          <option value="admin">Amministratore</option>
        </select>
      </div>
    </div>
    <div class="modal-footer">
      <button class="btn btn-ghost" onclick="closeModal('modal-nuovo-utente')">Annulla</button>
      <button class="btn btn-success" onclick="createUser()">Crea Utente</button>
    </div>
  </div>
</div>

<script>
// ── STATE ────────────────────────────────────────────────────
let TOKEN = localStorage.getItem('bm_token') || '';
let USER = JSON.parse(localStorage.getItem('bm_user') || '{}');
let currentPage = 1;
let currentProdottoId = null;
let searchTimeout = null;
let selectedFile = null;

// ── API ──────────────────────────────────────────────────────
async function api(method, path, body=null, formData=null) {
  // Rileggo sempre il token fresco da localStorage
  const token = localStorage.getItem('bm_token') || TOKEN;
  const opts = {
    method,
    headers: { 'Authorization': `Bearer ${token}` }
  };
  if (formData) {
    opts.body = formData;
  } else if (body) {
    opts.headers['Content-Type'] = 'application/json';
    opts.body = JSON.stringify(body);
  }
  try {
    const r = await fetch('/api' + path, opts);
    if (r.status === 401) { doLogout(); return null; }
    if (!r.ok) {
      const err = await r.json().catch(() => ({}));
      console.error('API error', r.status, err);
      return null;
    }
    return await r.json();
  } catch(e) {
    console.error('Fetch error:', e);
    return null;
  }
}

// ── AUTH ─────────────────────────────────────────────────────
async function doLogin() {
  const email = document.getElementById('login-email').value.trim();
  const pass = document.getElementById('login-password').value;
  const err = document.getElementById('login-error');
  err.style.display = 'none';

  const fd = new FormData();
  fd.append('username', email);
  fd.append('password', pass);

  const r = await fetch('/api/auth/login', { method: 'POST', body: fd });
  const data = await r.json();

  if (r.ok) {
    TOKEN = data.access_token;
    USER = { nome: data.nome, email: data.email, ruolo: data.ruolo };
    localStorage.setItem('bm_token', TOKEN);
    localStorage.setItem('bm_user', JSON.stringify(USER));
    initApp();
  } else {
    err.style.display = 'flex';
    err.textContent = data.detail || 'Credenziali non valide';
  }
}

function doLogout() {
  localStorage.removeItem('bm_token');
  localStorage.removeItem('bm_user');
  TOKEN = ''; USER = {};
  document.getElementById('login-screen').style.display = 'flex';
  document.getElementById('app').style.display = 'none';
}

document.getElementById('login-password').addEventListener('keydown', e => {
  if (e.key === 'Enter') doLogin();
});

// ── INIT ─────────────────────────────────────────────────────
function initApp() {
  document.getElementById('login-screen').style.display = 'none';
  document.getElementById('app').style.display = 'flex';

  document.getElementById('user-nome').textContent = USER.nome || '—';
  document.getElementById('user-email').textContent = USER.email || '';
  document.getElementById('user-badge').textContent = USER.ruolo === 'admin' ? '★ Admin' : 'Collaboratore';

  if (USER.ruolo === 'admin') {
    document.getElementById('nav-impostazioni').style.display = 'flex';
    document.getElementById('nav-utenti').style.display = 'flex';
  }

  loadDashboard();
  updateAILimit();

  // Ricarica se pagina già aperta
  if (TOKEN) {
    document.getElementById('login-screen').style.display = 'none';
    document.getElementById('app').style.display = 'flex';
  }
}

if (TOKEN) initApp();

// ── NAVIGATION ───────────────────────────────────────────────
function showView(name) {
  document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));

  document.getElementById('view-' + name).classList.add('active');
  document.querySelectorAll('.nav-item').forEach(n => {
    if (n.getAttribute('onclick') && n.getAttribute('onclick').includes(`'${name}'`))
      n.classList.add('active');
  });

  const titles = { dashboard: 'Dashboard', prodotti: 'Catalogo Prodotti',
    import: 'Import Excel', ai: 'AI Descrizioni', logs: 'Log Operazioni',
    impostazioni: 'Impostazioni', utenti: 'Gestione Utenti' };
  document.getElementById('topbar-title').textContent = titles[name] || name;

  if (name === 'prodotti') loadProdotti(1);
  if (name === 'logs') loadLogs();
  if (name === 'utenti') loadUtenti();
  if (name === 'ai') loadAIStats();
  if (name === 'dashboard') loadDashboard();
}

// ── DASHBOARD ────────────────────────────────────────────────
async function loadDashboard() {
  const d = await api('GET', '/dashboard');
  if (!d) return;

  document.getElementById('s-totale').textContent = d.totale.toLocaleString('it');
  document.getElementById('s-foto').textContent = d.con_foto.toLocaleString('it');
  document.getElementById('s-ai').textContent = d.con_ai.toLocaleString('it');
  document.getElementById('s-bc').textContent = d.inviati_bc.toLocaleString('it');
  document.getElementById('s-esauriti').textContent = d.esauriti.toLocaleString('it');
  document.getElementById('s-sotto').textContent = d.sottoscorta.toLocaleString('it');
  document.getElementById('topbar-count').textContent = d.totale.toLocaleString('it') + ' prodotti';

  const logList = document.getElementById('dash-logs');
  if (!d.logs.length) {
    logList.innerHTML = '<div class="empty-state"><p>Nessuna operazione</p></div>';
  } else {
    logList.innerHTML = d.logs.map(l => `
      <div class="log-item ${l.livello}">
        <span class="log-time">${l.data ? l.data.substring(11,19) : ''}</span>
        <span class="log-op">${l.operazione}</span>
        <span class="log-detail">${l.dettaglio}</span>
      </div>`).join('');
  }

  // Categorie
  const cats = await api('GET', '/statistiche/categorie');
  if (cats && cats.length) {
    const maxVal = Math.max(...cats.map(c => c.totale));
    document.getElementById('cat-chart').innerHTML = cats.slice(0,12).map(c => `
      <div style="background:var(--bg3);border:1px solid var(--border);border-radius:6px;padding:10px 14px;min-width:130px;">
        <div style="font-size:11px;color:var(--text3);margin-bottom:4px;">${c.categoria || 'N/D'}</div>
        <div style="font-size:18px;font-weight:700;font-family:var(--mono);color:var(--accent);">${c.totale.toLocaleString('it')}</div>
        <div style="height:3px;background:var(--border);border-radius:2px;margin-top:6px;">
          <div style="height:100%;width:${Math.round(c.totale/maxVal*100)}%;background:var(--accent);border-radius:2px;"></div>
        </div>
      </div>`).join('');
  }
}

// ── PRODOTTI ─────────────────────────────────────────────────
async function loadProdotti(page=1) {
  currentPage = page;
  const cerca = document.getElementById('search-input').value;
  const cat = document.getElementById('filter-cat').value;
  const stato = document.getElementById('filter-stato').value;
  const esauriti = document.getElementById('filter-esauriti').checked;
  const noai = document.getElementById('filter-noai').checked;

  const params = new URLSearchParams({ page, per_page: 50 });
  if (cerca) params.append('cerca', cerca);
  if (cat) params.append('categoria', cat);
  if (stato) params.append('stato', stato);
  if (esauriti) params.append('solo_esauriti', 'true');
  if (noai) params.append('solo_senza_ai', 'true');

  const tbody = document.getElementById('prodotti-tbody');
  tbody.innerHTML = '<tr><td colspan="9" style="text-align:center;padding:20px;color:var(--text3);">⏳ Caricamento...</td></tr>';

  const d = await api('GET', `/prodotti?${params}`);

  if (!d) {
    tbody.innerHTML = '<tr><td colspan="9"><div class="alert alert-error" style="margin:12px;">❌ Errore caricamento — riprova il login</div></td></tr>';
    return;
  }

  document.getElementById('prodotti-count').textContent = d.totale.toLocaleString('it') + ' prodotti';

  if (!d.prodotti || !d.prodotti.length) {
    tbody.innerHTML = '<tr><td colspan="9"><div class="empty-state"><div class="icon">📭</div><p>Nessun prodotto trovato</p></div></td></tr>';
    document.getElementById('pagination').innerHTML = '';
    return;
  }

  tbody.innerHTML = d.prodotti.map(p => `
    <tr style="cursor:pointer;" onclick="openProdotto(${p.id})">
      <td>${p.foto1 ? `<img class="td-img" src="${p.foto1}" onerror="this.style.display='none'">` : '<div class="td-img-ph">🖼️</div>'}</td>
      <td class="td-code">${p.codice || '—'}</td>
      <td class="td-title" title="${escHtml(p.titolo || '')}">${escHtml(p.titolo || '—')}</td>
      <td>
        <span style="font-size:11px;">${p.categoria1 || '—'}</span>
        ${p.categoria2 ? `<br><span style="font-size:10px;color:var(--text3);">${p.categoria2}</span>` : ''}
      </td>
      <td>${statoBadge(p.stato_bene)}</td>
      <td style="font-family:var(--mono);font-size:12px;">€${(p.prezzo_vendita||0).toFixed(2)}</td>
      <td>${qtBadge(p.quantita)}</td>
      <td>${p.ai_generata ? '<span class="badge badge-purple">🤖 AI</span>' : '<span class="badge badge-gray">—</span>'}</td>
      <td><button class="btn btn-ghost btn-sm" onclick="event.stopPropagation();openProdotto(${p.id})">Dettagli</button></td>
    </tr>`).join('');

  renderPagination(d.pagina, d.pagine);
}

function searchDebounce() {
  clearTimeout(searchTimeout);
  searchTimeout = setTimeout(() => loadProdotti(1), 350);
}

function renderPagination(current, total) {
  const p = document.getElementById('pagination');
  if (total <= 1) { p.innerHTML = ''; return; }
  let btns = '';
  const from = Math.max(1, current-2), to = Math.min(total, current+2);
  if (from > 1) btns += `<button class="page-btn" onclick="loadProdotti(1)">1</button>${from>2?'<span class="page-info">…</span>':''}`;
  for (let i=from;i<=to;i++) btns += `<button class="page-btn ${i===current?'active':''}" onclick="loadProdotti(${i})">${i}</button>`;
  if (to < total) btns += `${to<total-1?'<span class="page-info">…</span>':''}<button class="page-btn" onclick="loadProdotti(${total})">${total}</button>`;
  p.innerHTML = `<span class="page-info">Pag ${current}/${total}</span>${btns}`;
}

// ── PRODOTTO MODAL ───────────────────────────────────────────
async function openProdotto(id) {
  currentProdottoId = id;
  const p = await api('GET', `/prodotti/${id}`);
  if (!p) return;

  document.getElementById('modal-prodotto-title').textContent = p.titolo || p.codice || 'Prodotto';

  document.getElementById('modal-prodotto-body').innerHTML = `
    <div style="display:grid;grid-template-columns:120px 1fr;gap:16px;margin-bottom:16px;">
      ${p.foto1 ? `<img src="${p.foto1}" style="width:120px;height:120px;object-fit:cover;border-radius:6px;background:var(--bg3);">` : '<div style="width:120px;height:120px;background:var(--bg3);border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:40px;color:var(--text3);">🖼️</div>'}
      <div>
        <div style="font-family:var(--mono);font-size:12px;color:var(--accent);margin-bottom:4px;">${p.codice || '—'} ${p.ean ? '· EAN: '+p.ean : ''}</div>
        <div style="font-size:15px;font-weight:600;margin-bottom:8px;">${escHtml(p.titolo || '—')}</div>
        <div style="display:flex;flex-wrap:wrap;gap:6px;">
          ${statoBadge(p.stato_bene)}
          ${p.categoria1 ? `<span class="badge badge-blue">${p.categoria1}</span>` : ''}
          ${p.categoria2 ? `<span class="badge badge-gray">${p.categoria2}</span>` : ''}
          ${p.ai_generata ? '<span class="badge badge-purple">🤖 AI</span>' : ''}
        </div>
      </div>
    </div>
    <div class="form-row-3" style="margin-bottom:12px;">
      <div><div class="form-label">Prezzo</div><div style="font-size:18px;font-weight:700;font-family:var(--mono);">€${(p.prezzo_vendita||0).toFixed(2)}</div></div>
      <div><div class="form-label">Quantità</div><div>${qtBadge(p.quantita)}</div></div>
      <div><div class="form-label">Posizione</div><div style="font-family:var(--mono);font-size:13px;">${p.posizione_magazzino||'—'}</div></div>
    </div>
    ${p.autore?`<div style="margin-bottom:8px;"><span class="form-label">Autore/Artista:</span> ${escHtml(p.autore)}</div>`:''}
    ${p.anno?`<div style="margin-bottom:8px;"><span class="form-label">Anno:</span> ${p.anno}</div>`:''}
    ${p.produttore?`<div style="margin-bottom:8px;"><span class="form-label">Produttore:</span> ${escHtml(p.produttore)}</div>`:''}
    ${p.specifiche?`<div style="margin-bottom:8px;"><span class="form-label">Specifiche:</span> ${escHtml(p.specifiche)}</div>`:''}
    ${p.tag?`<div style="margin-bottom:12px;"><span class="form-label">Tag:</span> <span style="font-size:12px;color:var(--text2);">${escHtml(p.tag)}</span></div>`:''}
    ${p.descrizione ? `
    <div style="margin-bottom:8px;">
      <div class="form-label">Descrizione eBay ${p.ai_generata?'(AI)':''}</div>
      <div class="desc-preview">${p.descrizione}</div>
    </div>` : '<div style="padding:12px;background:var(--bg3);border-radius:6px;color:var(--text3);font-size:12px;">⚠️ Nessuna descrizione — clicca "Rigenera AI" per generarla</div>'}
  `;

  document.getElementById('modal-prodotto').style.display = 'flex';
}

async function rigeneraAI() {
  if (!currentProdottoId) return;
  const btn = document.getElementById('btn-rigenera-ai');
  btn.disabled = true;
  btn.textContent = '⏳ Generazione...';
  const r = await api('POST', `/prodotti/${currentProdottoId}/genera-ai`);
  btn.disabled = false;
  btn.textContent = '🤖 Rigenera AI';
  if (r && r.ok) {
    openProdotto(currentProdottoId);
  } else {
    alert(r?.detail || 'Errore generazione AI. Verifica la API Key in Impostazioni.');
  }
}

// ── IMPORT ───────────────────────────────────────────────────
function handleFileSelect(e) {
  const file = e.target.files[0];
  if (file) setSelectedFile(file);
}

function handleDrop(e) {
  e.preventDefault();
  document.getElementById('upload-area').classList.remove('drag');
  const file = e.dataTransfer.files[0];
  if (file) setSelectedFile(file);
}

function setSelectedFile(file) {
  selectedFile = file;
  document.getElementById('file-name').textContent = file.name;
  document.getElementById('file-selected').style.display = 'block';
  document.getElementById('btn-import').disabled = false;
}

async function doImport() {
  if (!selectedFile) return;
  const btn = document.getElementById('btn-import');
  btn.disabled = true;
  btn.textContent = '⏳ Invio file...';

  const fd = new FormData();
  fd.append('file', selectedFile);
  fd.append('genera_ai', 'false');
  fd.append('modalita', 'entrambi');

  document.getElementById('import-progress').style.display = 'block';
  document.getElementById('import-result').style.display = 'none';
  document.getElementById('import-status').textContent = 'Invio file al server...';
  document.getElementById('progress-fill').style.width = '5%';

  const r = await api('POST', '/import/excel', null, fd);

  if (!r || !r.ok) {
    btn.disabled = false;
    btn.textContent = '⬆️ Avvia Import';
    document.getElementById('import-result').style.display = 'block';
    document.getElementById('import-result').innerHTML = '<div class="alert alert-error">❌ Errore invio file. Riprova.</div>';
    return;
  }

  // File ricevuto — ora polling sullo stato
  btn.textContent = '⏳ Import in corso...';
  document.getElementById('import-status').textContent = 'Import avviato in background...';

  let pollInterval = setInterval(async () => {
    const status = await api('GET', '/import/status');
    if (!status) return;

    const pct = status.totale > 0
      ? Math.round((status.importati + status.aggiornati + status.skippati) / status.totale * 100)
      : 50;
    document.getElementById('progress-fill').style.width = Math.min(pct, 99) + '%';
    document.getElementById('import-status').textContent = status.messaggio || 'Elaborazione...';

    if (status.completato) {
      clearInterval(pollInterval);
      document.getElementById('progress-fill').style.width = '100%';
      btn.disabled = false;
      btn.textContent = '⬆️ Avvia Import';

      const errHtml = status.errori && status.errori.length
        ? `<div style="margin-top:8px;font-size:12px;color:var(--red);">⚠️ ${status.errori.slice(0,5).join('<br>')}</div>` : '';

      document.getElementById('import-result').style.display = 'block';
      document.getElementById('import-result').innerHTML = `
        <div class="alert alert-success">
          ✅ <strong>Import completato!</strong><br>
          Nuovi: <strong>${status.importati}</strong> · 
          Aggiornati: <strong>${status.aggiornati}</strong> · 
          Totale righe: <strong>${status.totale}</strong> · 
          Errori: <strong>${status.errori ? status.errori.length : 0}</strong>
          ${errHtml}
        </div>`;
      loadDashboard();
    }
  }, 2000); // polling ogni 2 secondi
}

// ── AI STATS ─────────────────────────────────────────────────
async function loadAIStats() {
  const d = await api('GET', '/dashboard');
  if (!d) return;
  document.getElementById('ai-count-done').textContent = d.con_ai.toLocaleString('it');
  document.getElementById('ai-count-missing').textContent = (d.totale - d.con_ai).toLocaleString('it');
}

function updateAILimit() {
  const limit = parseInt(document.getElementById('ai-limit')?.value || 50);
  const el = document.getElementById('ai-cost');
  if (el) el.textContent = '€' + (limit * 0.001).toFixed(3);
}
document.addEventListener('input', e => { if (e.target.id === 'ai-limit') updateAILimit(); });

async function generaAIBatch() {
  const limit = parseInt(document.getElementById('ai-limit').value || 50);
  const cat = document.getElementById('ai-cat-filter').value;
  const btn = document.getElementById('btn-genera-ai');
  btn.disabled = true;

  // Prendi prodotti senza AI
  const params = new URLSearchParams({ per_page: limit, solo_senza_ai: 'true' });
  if (cat) params.append('categoria', cat);
  const lista = await api('GET', `/prodotti?${params}`);
  if (!lista || !lista.prodotti.length) {
    alert('Nessun prodotto da elaborare!');
    btn.disabled = false;
    return;
  }

  const prodotti = lista.prodotti;
  document.getElementById('ai-progress').style.display = 'block';

  for (let i=0; i<prodotti.length; i++) {
    const p = prodotti[i];
    document.getElementById('ai-status').textContent = `Elaboro: ${p.titolo?.substring(0,50) || p.codice}...`;
    document.getElementById('ai-counter').textContent = `${i+1} / ${prodotti.length}`;
    document.getElementById('ai-progress-fill').style.width = Math.round((i+1)/prodotti.length*100) + '%';
    await api('POST', `/prodotti/${p.id}/genera-ai`);
    await new Promise(r => setTimeout(r, 500)); // pausa anti-rate-limit
  }

  document.getElementById('ai-status').textContent = `✅ Completato! ${prodotti.length} descrizioni generate.`;
  btn.disabled = false;
  loadAIStats();
  loadDashboard();
}

// ── LOGS ─────────────────────────────────────────────────────
async function loadLogs() {
  const logs = await api('GET', '/logs?limit=200');
  if (!logs) return;
  const tbody = document.getElementById('logs-tbody');
  if (!logs.length) {
    tbody.innerHTML = '<tr><td colspan="4"><div class="empty-state"><p>Nessun log</p></div></td></tr>';
    return;
  }
  tbody.innerHTML = logs.map(l => `
    <tr>
      <td style="font-family:var(--mono);font-size:11px;color:var(--text3);white-space:nowrap;">${l.data?l.data.replace('T',' ').substring(0,19):''}</td>
      <td><span class="badge ${l.livello==='success'?'badge-green':l.livello==='error'?'badge-red':l.livello==='warning'?'badge-orange':'badge-blue'}">${l.operazione}</span></td>
      <td style="font-size:12px;color:var(--text2);">${escHtml(l.dettaglio)}</td>
      <td style="font-size:11px;color:var(--text3);">${l.utente||'—'}</td>
    </tr>`).join('');
}

// ── CONFIG ───────────────────────────────────────────────────
async function saveConfig(chiave, inputId) {
  const valore = document.getElementById(inputId).value.trim();
  if (!valore) { alert('Inserisci un valore'); return; }
  const r = await api('POST', '/config', { chiave, valore });
  const el = document.getElementById('config-alert');
  if (r && r.ok) {
    el.innerHTML = '<div class="alert alert-success">✅ Configurazione salvata!</div>';
    document.getElementById(inputId).value = '';
  } else {
    el.innerHTML = '<div class="alert alert-error">❌ Errore salvataggio</div>';
  }
  setTimeout(() => el.innerHTML='', 3000);
}

// ── UTENTI ───────────────────────────────────────────────────
async function loadUtenti() {
  const utenti = await api('GET', '/utenti');
  if (!utenti) return;
  document.getElementById('utenti-tbody').innerHTML = utenti.map(u => `
    <tr>
      <td>${escHtml(u.nome)}</td>
      <td style="font-family:var(--mono);font-size:12px;">${u.email}</td>
      <td><span class="badge ${u.ruolo==='admin'?'badge-blue':'badge-gray'}">${u.ruolo}</span></td>
      <td><span class="badge ${u.attivo?'badge-green':'badge-red'}">${u.attivo?'Attivo':'Disattivato'}</span></td>
      <td>${u.email !== USER.email ? `<button class="btn btn-danger btn-sm" onclick="deleteUser(${u.id})">Elimina</button>` : ''}</td>
    </tr>`).join('');
}

function openNewUser() {
  document.getElementById('modal-nuovo-utente').style.display = 'flex';
}

async function createUser() {
  const nome = document.getElementById('new-nome').value.trim();
  const email = document.getElementById('new-email').value.trim();
  const password = document.getElementById('new-password').value;
  const ruolo = document.getElementById('new-ruolo').value;
  if (!nome || !email || !password) { alert('Compila tutti i campi'); return; }
  const r = await api('POST', '/utenti', { nome, email, password, ruolo });
  if (r && r.ok) {
    closeModal('modal-nuovo-utente');
    loadUtenti();
  } else {
    alert(r?.detail || 'Errore creazione utente');
  }
}

async function deleteUser(id) {
  if (!confirm('Eliminare questo utente?')) return;
  await api('DELETE', `/utenti/${id}`);
  loadUtenti();
}

// ── MODAL ────────────────────────────────────────────────────
function closeModal(id) {
  document.getElementById(id).style.display = 'none';
}

// ── UTILS ────────────────────────────────────────────────────
function escHtml(s) {
  return String(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}

function statoBadge(stato) {
  if (!stato) return '<span class="badge badge-gray">—</span>';
  const map = {
    'Nuovo': 'badge-green', 'Sigillato': 'badge-green',
    'Come nuovo': 'badge-green', 'Ottime condizioni': 'badge-green',
    'Buone condizioni': 'badge-blue', 'Condizioni accettabili': 'badge-orange',
    'Usato': 'badge-orange'
  };
  return `<span class="badge ${map[stato]||'badge-gray'}" style="font-size:10px;">${stato}</span>`;
}

function qtBadge(qt) {
  qt = parseInt(qt) || 0;
  if (qt === 0) return '<span class="badge badge-red">Esaurito</span>';
  if (qt <= 2) return `<span class="badge badge-orange">${qt}</span>`;
  return `<span class="badge badge-green">${qt}</span>`;
}
</script>
</body>
</html>
