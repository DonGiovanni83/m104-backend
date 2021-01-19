from typing import List

from api.data import Klasse
from repositories.abstract import AbstractKlassenRepository


class KlassenRepository(AbstractKlassenRepository):
    @staticmethod
    def get_klassen() -> List[Klasse]:
        pass

    @staticmethod
    def create_klasse(klasse) -> int:
        pass

    @staticmethod
    def delete_klasse() -> bool:
        pass
