from typing import List

from api.data import *
from api.mutations import Mutation


@strawberry.type
class Query:
    klassen: List[Klasse]


