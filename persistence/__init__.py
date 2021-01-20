from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Adresse(Base):
    __tablename__ = 'adresse'

    id = Column(Integer, primary_key=True)
    ort = Column(String(50), default="")
    plz = Column(Integer, default=0000)
    adresse_1 = Column(String(50), default="")
    adresse_2 = Column(String(50), nullable=True)
    tel_g = Column(String(50), nullable=True)
    tel_m = Column(String(50), nullable=True)
    email_1 = Column(String(50), nullable=True)
    email_2 = Column(String(50), nullable=True)

    schule = relationship("Schule", uselist=False, back_populates="adresse", lazy='joined')


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    vorname = Column(String(50))
    adresse_id = Column(Integer, ForeignKey('adresse.id'))


class Schule(Base):
    __tablename__ = 'schule'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    adresse_id = Column(Integer, ForeignKey('adresse.id'))
    adresse = relationship("Adresse", back_populates='schule', lazy='joined')


class Klasse(Base):
    __tablename__ = 'klasse'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    schule_id = Column(Integer, ForeignKey('schule.id'))


class Modul(Base):
    __tablename__ = 'modul'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    schule_id = Column(Integer, ForeignKey('schule.id'))


class Firma(Base):
    __tablename__ = 'firma'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    adresse_id = Column(Integer, ForeignKey('adresse.id'))


class ABV(Person):
    __tablename__ = 'abv'
    id = Column(Integer, ForeignKey('person.id'), primary_key=True)
    firmen_id = Column(Integer, ForeignKey('firma.id'))


class Schueler(Person):
    __tablename__ = 'schueler'
    id = Column(Integer, ForeignKey('person.id'), primary_key=True)
    schueler_id = Column(Integer, unique=True)
    firma_id = Column(Integer, ForeignKey('firma.id'))
    abv_id = Column(Integer, ForeignKey('abv.id'))
    klasse_id = Column(Integer, ForeignKey('klasse.id'))
