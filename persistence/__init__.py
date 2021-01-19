from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Adresse(Base):
    __tablename__ = 'adressen'

    id = Column(Integer, Sequence('addr_id_seq'), primary_key=True)
    ort = Column(String(50))
    plz = Column(Integer)
    adresse_1 = Column(String(50))
    adresse_2 = Column(String(50), nullable=True)
    tel_g = Column(String(50), nullable=True)
    tel_m = Column(String(50), nullable=True)
    email_1 = Column(String(50), nullable=True)
    email_2 = Column(String(50), nullable=True)


class Person(Base):
    __tablename__ = 'personen'

    id = Column(Integer, Sequence('person_id_seq'), primary_key=True)
    name = Column(String(50))
    vorname = Column(String(50))
    adresse_id = Column(Integer, ForeignKey('adressen.id'))


class Schule(Base):
    __tablename__ = 'schulen'

    id = Column(Integer, Sequence('schulen_id_seq'), primary_key=True)
    name = Column(String(100))
    adresse_id = Column(Integer, ForeignKey('adressen.id'))


class Klasse(Base):
    __tablename__ = 'klassen'

    id = Column(Integer, Sequence('klasse_id_seq'), primary_key=True)
    name = Column(String(20))
    schule_id = Column(Integer, ForeignKey('schulen.id'))


class Modul(Base):
    __tablename__ = 'module'
    id = Column(Integer, Sequence('modul_id_seq'), primary_key=True)
    name = Column(String(100))
    schule_id = Column(Integer, ForeignKey('schulen.id'))


class Firma(Base):
    __tablename__ = 'firmen'
    id = Column(Integer, Sequence('firmen_id_seq'), primary_key=True)
    name = Column(String(100))
    adresse_id = Column(Integer, ForeignKey('adressen.id'))


class ABV(Person):
    __tablename__ = 'abvs'
    id = Column(Integer, ForeignKey('personen.id'), primary_key=True)
    firmen_id = Column(Integer, ForeignKey('firmen.id'))


class Schueler(Person):
    __tablename__ = 'schueler'
    id = Column(Integer, ForeignKey('personen.id'), primary_key=True)
    schueler_id = Column(Integer, unique=True)
    firma_id = Column(Integer, ForeignKey('firmen.id'))
    abv_id = Column(Integer, ForeignKey('abvs.id'))
    klasse_id = Column(Integer, ForeignKey('klassen.id'))
