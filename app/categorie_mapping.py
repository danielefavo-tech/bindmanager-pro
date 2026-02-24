"""
MAPPATURA CATEGORIE: Biban/Bman → BindCommerce
Categoria 1° livello + Categoria 2° livello → percorso BindCommerce
Formato: (cat1_biban, cat2_biban) → (cat1_bc, cat2_bc)
"""

# ─────────────────────────────────────────────────────────────────
# MAPPATURA PRINCIPALE
# chiave: (categoria1.lower(), categoria2.lower())
# valore: {"cat1": "...", "cat2": "..."} — nomi ESATTI BindCommerce
# ─────────────────────────────────────────────────────────────────

MAPPING: dict = {

    # ── CD ───────────────────────────────────────────────────────
    ("cd", "altri generi"):              {"cat1": "Cd", "cat2": "Altri generi"},
    ("cd", "altro"):                     {"cat1": "Cd", "cat2": "Altri generi"},
    ("cd", "classica e lirica"):         {"cat1": "Cd", "cat2": "Classica e Lirica"},
    ("cd", "classica"):                  {"cat1": "Cd", "cat2": "Classica e Lirica"},
    ("cd", "lirica"):                    {"cat1": "Cd", "cat2": "Classica e Lirica"},
    ("cd", "colonne sonore"):            {"cat1": "Cd", "cat2": "Colonne sonore"},
    ("cd", "dance e elettronica"):       {"cat1": "Cd", "cat2": "Dance e Elettronica"},
    ("cd", "dance"):                     {"cat1": "Cd", "cat2": "Dance e Elettronica"},
    ("cd", "elettronica"):               {"cat1": "Cd", "cat2": "Dance e Elettronica"},
    ("cd", "disco"):                     {"cat1": "Cd", "cat2": "Disco"},  # manca in bc ma usiamo Altri generi
    ("cd", "folk - country - world music"): {"cat1": "Cd", "cat2": "Altri generi"},
    ("cd", "folk"):                      {"cat1": "Cd", "cat2": "Altri generi"},
    ("cd", "country"):                   {"cat1": "Cd", "cat2": "Altri generi"},
    ("cd", "world music"):               {"cat1": "Cd", "cat2": "Altri generi"},
    ("cd", "jazz - blues  r&b e soul"):  {"cat1": "Cd", "cat2": "Jazz - Blues R&B e Soul"},
    ("cd", "jazz - blues r&b e soul"):   {"cat1": "Cd", "cat2": "Jazz - Blues R&B e Soul"},
    ("cd", "jazz"):                      {"cat1": "Cd", "cat2": "Jazz - Blues R&B e Soul"},
    ("cd", "blues"):                     {"cat1": "Cd", "cat2": "Jazz - Blues R&B e Soul"},
    ("cd", "r&b"):                       {"cat1": "Cd", "cat2": "Jazz - Blues R&B e Soul"},
    ("cd", "soul"):                      {"cat1": "Cd", "cat2": "Jazz - Blues R&B e Soul"},
    ("cd", "funk"):                      {"cat1": "Cd", "cat2": "Jazz - Blues R&B e Soul"},
    ("cd", "hip hop"):                   {"cat1": "Cd", "cat2": "Jazz - Blues R&B e Soul"},
    ("cd", "metal"):                     {"cat1": "Cd", "cat2": "Metal"},
    ("cd", "pop & rock internazionale"): {"cat1": "Cd", "cat2": "Pop & Rock internazionale"},
    ("cd", "pop & rock italiano"):       {"cat1": "Cd", "cat2": "Pop & Rock Italiano"},
    ("cd", "reggae e ska"):              {"cat1": "Cd", "cat2": "Reggae e Ska"},
    ("cd", "reggae"):                    {"cat1": "Cd", "cat2": "Reggae e Ska"},
    ("cd", "ska"):                       {"cat1": "Cd", "cat2": "Reggae e Ska"},
    ("cd", ""):                          {"cat1": "Cd", "cat2": "Altri generi"},

    # ── VINILE 33 GIRI ───────────────────────────────────────────
    ("dischi vinile 33 giri", "altri generi"):          {"cat1": "Dischi vinile 33 giri", "cat2": "Altri generi"},
    ("dischi vinile 33 giri", "blues - r&b e soul - funk"): {"cat1": "Dischi vinile 33 giri", "cat2": "Blues - R&B e Soul - Funk"},
    ("dischi vinile 33 giri", "classica e lirica"):     {"cat1": "Dischi vinile 33 giri", "cat2": "Classica e Lirica"},
    ("dischi vinile 33 giri", "colonne sonore"):        {"cat1": "Dischi vinile 33 giri", "cat2": "Colonne sonore"},
    ("dischi vinile 33 giri", "dance e elettronica"):   {"cat1": "Dischi vinile 33 giri", "cat2": "Dance e Elettronica"},
    ("dischi vinile 33 giri", "disco"):                 {"cat1": "Dischi vinile 33 giri", "cat2": "Disco"},
    ("dischi vinile 33 giri", "folk - country - world music"): {"cat1": "Dischi vinile 33 giri", "cat2": "Folk - Country - World Music"},
    ("dischi vinile 33 giri", "jazz"):                  {"cat1": "Dischi vinile 33 giri", "cat2": "Jazz"},
    ("dischi vinile 33 giri", "metal"):                 {"cat1": "Dischi vinile 33 giri", "cat2": "Metal"},
    ("dischi vinile 33 giri", "pop & rock internazionale"): {"cat1": "Dischi vinile 33 giri", "cat2": "Pop & Rock internazionale"},
    ("dischi vinile 33 giri", "pop & rock italiano"):   {"cat1": "Dischi vinile 33 giri", "cat2": "Pop & Rock Italiano"},
    ("dischi vinile 33 giri", "reggae e ska"):          {"cat1": "Dischi vinile 33 giri", "cat2": "Reggae e Ska"},
    ("dischi vinile 33 giri", ""):                      {"cat1": "Dischi vinile 33 giri", "cat2": "Altri generi"},
    # alias brevi
    ("vinile 33", "pop & rock internazionale"):         {"cat1": "Dischi vinile 33 giri", "cat2": "Pop & Rock internazionale"},
    ("33 giri", "pop & rock internazionale"):           {"cat1": "Dischi vinile 33 giri", "cat2": "Pop & Rock internazionale"},

    # ── VINILE 45 GIRI ───────────────────────────────────────────
    ("dischi vinile 45 giri", "altri generi"):          {"cat1": "Dischi Vinile 45 giri", "cat2": "Altri generi"},
    ("dischi vinile 45 giri", "bambini"):               {"cat1": "Dischi Vinile 45 giri", "cat2": "Bambini"},
    ("dischi vinile 45 giri", "classica e lirica"):     {"cat1": "Dischi Vinile 45 giri", "cat2": "Classica e Lirica"},
    ("dischi vinile 45 giri", "colonne sonore"):        {"cat1": "Dischi Vinile 45 giri", "cat2": "Colonne sonore"},
    ("dischi vinile 45 giri", "dance e elettronica"):   {"cat1": "Dischi Vinile 45 giri", "cat2": "Dance e Elettronica"},
    ("dischi vinile 45 giri", "disco"):                 {"cat1": "Dischi Vinile 45 giri", "cat2": "Disco"},
    ("dischi vinile 45 giri", "folk - country - world music"): {"cat1": "Dischi Vinile 45 giri", "cat2": "Folk - Country - World Music"},
    ("dischi vinile 45 giri", "jazz - blues r&b e soul"): {"cat1": "Dischi Vinile 45 giri", "cat2": "Jazz - Blues R&B e Soul"},
    ("dischi vinile 45 giri", "metal"):                 {"cat1": "Dischi Vinile 45 giri", "cat2": "Metal"},
    ("dischi vinile 45 giri", "pop & rock internazionale"): {"cat1": "Dischi Vinile 45 giri", "cat2": "Pop & Rock internazionale"},
    ("dischi vinile 45 giri", "pop & rock italiano"):   {"cat1": "Dischi Vinile 45 giri", "cat2": "Pop & Rock Italiano"},
    ("dischi vinile 45 giri", "reggae e ska"):          {"cat1": "Dischi Vinile 45 giri", "cat2": "Reggae e Ska"},
    ("dischi vinile 45 giri", ""):                      {"cat1": "Dischi Vinile 45 giri", "cat2": "Altri generi"},
    ("45 giri", "pop & rock internazionale"):           {"cat1": "Dischi Vinile 45 giri", "cat2": "Pop & Rock internazionale"},

    # ── MUSICASSETTE ─────────────────────────────────────────────
    ("musicassette", "pop & rock internazionale"):      {"cat1": "Musicassette", "cat2": "Pop & Rock internazionale"},
    ("musicassette", "pop & rock italiano"):            {"cat1": "Musicassette", "cat2": "Pop & Rock Italiano"},
    ("musicassette", ""):                               {"cat1": "Musicassette", "cat2": "Pop & Rock internazionale"},

    # ── FILM E DVD ───────────────────────────────────────────────
    ("film e dvd", "cartoni animati"):                  {"cat1": "Film e DVD", "cat2": "Cartoni animati"},
    ("film e dvd", "azione e avventura"):               {"cat1": "Film e DVD", "cat2": "Cinema internazionale"},
    ("film e dvd", "classici e cult movie"):            {"cat1": "Film e DVD", "cat2": "Cinema internazionale"},
    ("film e dvd", "commedie"):                         {"cat1": "Film e DVD", "cat2": "Cinema internazionale"},
    ("film e dvd", "documentari"):                      {"cat1": "Film e DVD", "cat2": "Cinema internazionale"},
    ("film e dvd", "drammatici"):                       {"cat1": "Film e DVD", "cat2": "Cinema internazionale"},
    ("film e dvd", "horror"):                           {"cat1": "Film e DVD", "cat2": "Cinema internazionale"},
    ("film e dvd", "musicali"):                         {"cat1": "Film e DVD", "cat2": "Cinema internazionale"},
    ("film e dvd", "thriller e gialli"):                {"cat1": "Film e DVD", "cat2": "Cinema internazionale"},
    ("film e dvd", "cinema italiano"):                  {"cat1": "Film e DVD", "cat2": "Cinema italiano"},
    ("film e dvd", "fantascienza e fantasy"):           {"cat1": "Film e DVD", "cat2": "Fantascienza e Fantasy"},
    ("film e dvd", "film per la famiglia"):             {"cat1": "Film e DVD", "cat2": "Film per la famiglia"},
    ("film e dvd", ""):                                 {"cat1": "Film e DVD", "cat2": "Cinema internazionale"},
    ("dvd", ""):                                        {"cat1": "Film e DVD", "cat2": "Cinema internazionale"},

    # ── LIBRI E RIVISTE ──────────────────────────────────────────
    ("libri e riviste", "narrativa e poesia"):          {"cat1": "Libri e Riviste", "cat2": "Libri Narrativa e Poesia"},
    ("libri e riviste", "romanzi"):                     {"cat1": "Libri e Riviste", "cat2": "Libri Narrativa e Poesia"},
    ("libri e riviste", "gialli"):                      {"cat1": "Libri e Riviste", "cat2": "Libri Narrativa e Poesia"},
    ("libri e riviste", "fantascienza"):                {"cat1": "Libri e Riviste", "cat2": "Libri Narrativa e Poesia"},
    ("libri e riviste", "horror"):                      {"cat1": "Libri e Riviste", "cat2": "Libri Narrativa e Poesia"},
    ("libri e riviste", "saggistica"):                  {"cat1": "Libri e Riviste", "cat2": "Saggistica"},
    ("libri e riviste", "manuali"):                     {"cat1": "Libri e Riviste", "cat2": "Manuali, Corsi, Libri di testo"},
    ("libri e riviste", "manuali, corsi, libri di testo"): {"cat1": "Libri e Riviste", "cat2": "Manuali, Corsi, Libri di testo"},
    ("libri e riviste", "riviste e giornali"):          {"cat1": "Libri e Riviste", "cat2": "Riviste e Giornali"},
    ("libri e riviste", "libri per ragazzi"):           {"cat1": "Libri e Riviste", "cat2": "Libri per Ragazzi"},
    ("libri e riviste", "lotti e stock libri"):         {"cat1": "Libri e Riviste", "cat2": "Lotti e Stock Libri"},
    ("libri e riviste", ""):                            {"cat1": "Libri e Riviste", "cat2": "Libri Narrativa e Poesia"},
    ("libri", ""):                                      {"cat1": "Libri e Riviste", "cat2": "Libri Narrativa e Poesia"},

    # ── STRUMENTI MUSICALI ───────────────────────────────────────
    ("strumenti musicali", "altri strumenti e accessori"): {"cat1": "Strumenti musicali", "cat2": "Altri Strumenti e accessori"},
    ("strumenti musicali", "spartiti"):                 {"cat1": "Strumenti musicali", "cat2": "Manuali e Corsi"},
    ("strumenti musicali", ""):                         {"cat1": "Strumenti musicali", "cat2": "Altri Strumenti e accessori"},

    # ── VIDEOGIOCHI ──────────────────────────────────────────────
    ("videogiochi", "giochi"):                          {"cat1": "VIDEOGIOCHI", "cat2": "Videogiochi e console"},
    ("videogiochi", ""):                                {"cat1": "VIDEOGIOCHI", "cat2": "Videogiochi e console"},

    # ── FUMETTI ──────────────────────────────────────────────────
    ("fumetti", ""):                                    {"cat1": "Fumetti", "cat2": "Altri fumetti"},
    ("fumetti", "altri fumetti"):                       {"cat1": "Fumetti", "cat2": "Altri fumetti"},

    # ── MODELLISMO ───────────────────────────────────────────────
    ("modellismo statico", "aerei"):                    {"cat1": "Modellismo Statico", "cat2": "Aerei"},
    ("modellismo statico", "auto"):                     {"cat1": "Modellismo Statico", "cat2": "Auto"},
    ("modellismo statico", "moto"):                     {"cat1": "Modellismo Statico", "cat2": "Moto"},
    ("modellismo statico", "treni"):                    {"cat1": "Modellismo Statico", "cat2": "Treni"},
    ("modellismo statico", "soldatini"):                {"cat1": "Modellismo Statico", "cat2": "Soldatini"},
    ("modellismo statico", ""):                         {"cat1": "Modellismo Statico", "cat2": "Auto"},

    # ── LOCANDINE ────────────────────────────────────────────────
    ("locandine e manifesti", "film italiani"):         {"cat1": "Locandine e Manifesti", "cat2": "Film Italiani"},
    ("locandine e manifesti", "film stranieri"):        {"cat1": "Locandine e Manifesti", "cat2": "Film Stranieri"},
    ("locandine e manifesti", ""):                      {"cat1": "Locandine e Manifesti", "cat2": "Film Stranieri"},
}

# Default di fallback se non trovato
FALLBACK = {"cat1": "Altro", "cat2": "Collezioni diverse"}


def mappa_categoria(cat1: str, cat2: str = "") -> dict:
    """
    Restituisce il dict {cat1, cat2} per BindCommerce.
    Cerca prima la coppia esatta, poi solo cat1, poi fallback.
    """
    c1 = (cat1 or "").strip().lower()
    c2 = (cat2 or "").strip().lower()

    # 1. Coppia esatta
    result = MAPPING.get((c1, c2))
    if result:
        return result

    # 2. Solo cat1 con stringa vuota
    result = MAPPING.get((c1, ""))
    if result:
        return result

    # 3. Fallback generico
    return FALLBACK


def get_tutte_cat1_bc() -> list:
    """Ritorna lista unica di tutte le cat1 BindCommerce disponibili."""
    return sorted(set(v["cat1"] for v in MAPPING.values()))


def get_cat2_per_cat1(cat1_bc: str) -> list:
    """Ritorna le cat2 disponibili per una cat1 BindCommerce."""
    return sorted(set(
        v["cat2"] for v in MAPPING.values()
        if v["cat1"] == cat1_bc
    ))
