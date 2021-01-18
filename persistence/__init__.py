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
    adresse_2 = Column(String(50), null=True)
    tel_g = Column(String(50), null=True)
    tel_m = Column(String(50), null=True)
    email_1 = Column(String(50), null=True)
    email_2 = Column(String(50), null=True)

    def __init__(self, name, model, doors):
        self.name = name
        self.model = model
        self.doors = doors


class Person(Base):
    __tablename__ = 'personen'

    id = Column(Integer, Sequence('person_id_seq'), primary_key=True)
    name = Column(String(50))
    vorname = Column(String(50))
    adresse_id = Column(Integer, ForeignKey('adressen.id'))

    adresse = relationship("Adresse", back_populates="personen")


class Schule(Base):
    __tablename__ = 'schulen'

    id = Column(Integer, Sequence('schulen_id_seq'), primary_key=True)
    name = Column(String(100))
    adresse_id = Column(Integer, ForeignKey('adressen.id'))

    adresse = relationship("Adresse", back_populates="schulen")


class Klasse(Base):
    __tablename__ = 'klassen'

    id = Column(Integer, Sequence('klasse_id_seq'), primary_key=True)
    name = Column(String(20))
    schule_id = Column(Integer, ForeignKey('schulen.id'))

    schule = relationship("Schule", back_populates="klassen")


class Modul(Base):
    __tablename__ = 'module'
    id = Column(Integer, Sequence('modul_id_seq'), primary_key=True)
    name = Column(String(100))
    schule_id = Column(Integer, ForeignKey('schulen.id'))

    schule = relationship("Schule", back_populates="module")


class Firma(Base):
    __tablename__ = 'firmen'
    id = Column(Integer, Sequence('firmen_id_seq'), primary_key=True)
    name = Column(String(100))
    adresse_id = Column(Integer, ForeignKey('adressen.id'))

    adresse = relationship("Adresse", back_populates="firmen")


class ABV(Person):
    __tablename__ = 'abvs'
    id = Column(Integer, ForeignKey('personen.id'), primary_key=True)
    person = relationship("Person", back_populates="abvs")
    firmen_id = Column(Integer, ForeignKey('firmen.id'))
    firmen = relationship("Firma", back_populates="abvs")


class Schueler(Person):
    __tablename__ = 'schueler'
    id = Column(Integer, ForeignKey('personen.id'), primary_key=True)
    schueler_id = Column(Integer, unique=True)
    person = relationship("Person", back_populates="schueler")
    firma_id = Column(Integer, ForeignKey('firmen.id'))
    firma = relationship("Firma", back_populates="schueler")
    abv_id = Column(Integer, ForeignKey('abvs.id'))
    abv = relationship("ABV", back_populates="schueler")
