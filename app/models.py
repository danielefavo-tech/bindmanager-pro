from sqlalchemy import Column, Integer, String, Float, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    nome = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    ruolo = Column(String, default="collaboratore")  # admin | collaboratore
    attivo = Column(Boolean, default=True)
    creato_il = Column(DateTime(timezone=True), server_default=func.now())

class Prodotto(Base):
    __tablename__ = "prodotti"
    id = Column(Integer, primary_key=True, index=True)
    codice = Column(String, unique=True, index=True)
    ean = Column(String, index=True)
    titolo = Column(String)
    autore = Column(String)
    anno = Column(String)
    categoria1 = Column(String)
    categoria2 = Column(String)
    categoria3 = Column(String)
    categoria4 = Column(String)
    tipo_prodotto = Column(String)
    produttore = Column(String)
    stato_bene = Column(String)
    specifiche = Column(String)
    dettaglio_stato = Column(String)
    prezzo_acquisto = Column(Float, default=0)
    prezzo_vendita = Column(Float, default=0)
    quantita = Column(Integer, default=0)
    posizione_magazzino = Column(String)
    descrizione_breve = Column(Text)
    descrizione = Column(Text)          # descrizione HTML eBay (da Claude)
    descrizione_sito = Column(Text)     # descrizione narrativa sito (da Claude)
    tag = Column(Text)
    note = Column(Text)
    foto1 = Column(String)
    foto2 = Column(String)
    foto3 = Column(String)
    ai_generata = Column(Boolean, default=False)
    bindcommerce_inviato = Column(Boolean, default=False)
    bindcommerce_id = Column(String)
    creato_il = Column(DateTime(timezone=True), server_default=func.now())
    aggiornato_il = Column(DateTime(timezone=True), onupdate=func.now())

class Log(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True)
    operazione = Column(String)
    dettaglio = Column(Text)
    livello = Column(String, default="info")  # info | warning | error | success
    utente_email = Column(String)
    creato_il = Column(DateTime(timezone=True), server_default=func.now())

class Configurazione(Base):
    __tablename__ = "configurazione"
    id = Column(Integer, primary_key=True, index=True)
    chiave = Column(String, unique=True)
    valore = Column(Text)
