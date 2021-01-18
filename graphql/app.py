from typing import List

import strawberry


@strawberry.type
class Adresse:
    id: int
    ort: str
    plz: int
    adresse_1: str
    adresse_2: str
    tel_g: str
    tel_m: str
    email_1: str
    email_2: str


@strawberry.type
class Schule:
    id: int
    name: str
    adresse: Adresse


@strawberry.type
class Klasse:
    id: int
    name: str
    schule: Schule


@strawberry.type
class Modul:
    id: int
    name: str
    schule: Schule


@strawberry.type
class Firma:
    id: int
    name: str
    adresse: Adresse


@strawberry.type
class Person:
    id: int
    name: str
    vorname: str
    adresse: Adresse


@strawberry.type
class ABV:
    id: int
    person: Person
    firma: Firma


@strawberry.type
class Schueler:
    id: int
    schueler_id: int
    person: Person
    firma: Firma
    abv: ABV


@strawberry.type
class Query:
    adressen: List[Adresse]


schema = strawberry.Schema(query=Query)
