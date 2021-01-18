from typing import List

import strawberry
from strawberry.utils import typing


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
class Query:
    adressen: List[Adresse]


schema = strawberry.Schema(query=Query)
