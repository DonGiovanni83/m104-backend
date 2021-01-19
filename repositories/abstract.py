from abc import ABC, abstractmethod
from typing import List

from api.data import Klasse, Modul, Schueler, Schule, Adresse
from persistence import database

class AbstractKlassenRepository(ABC):

    @abstractmethod
    async def get_klassen(self) -> List[Klasse]:
        ...

    @abstractmethod
    async def create_klasse(self, klasse) -> int:
        ...

    @abstractmethod
    async def delete_klasse(self) -> bool:
        ...

    def __init__(self):
        self.session = database.get_session()


class AbstractSchulenRepository(ABC):

    @abstractmethod
    async def get_schulen(self) -> List[Schule]:
        ...

    @abstractmethod
    async def find_schule(self, sid) -> Schule:
        ...

    @abstractmethod
    async def create_schule(self, schule) -> int:
        ...

    @abstractmethod
    async def delete_schule(self) -> bool:
        ...

    def __init__(self):
        self.session = database.get_session()


class AbstractAdressenRepository(ABC):

    @abstractmethod
    async def get_adressen(self) -> List[Adresse]:
        ...

    @abstractmethod
    async def find_adresse(self, sid) -> Adresse:
        ...

    @abstractmethod
    async def create_adresse(self, adresse) -> int:
        ...

    @abstractmethod
    async def delete_adresse(self) -> bool:
        ...

    def __init__(self):
        self.session = database.get_session()


class AbstractModuleRepository(ABC):

    @abstractmethod
    async def get_module(self) -> List[Modul]:
        ...

    @abstractmethod
    async def create_modul(self) -> int:
        ...

    @abstractmethod
    async def delete_modul(self) -> bool:
        ...

    def __init__(self):
        self.session = database.get_session()


class AbstractSchuelerRepository(ABC):

    @abstractmethod
    async def get_schueler(self) -> List[Schueler]:
        ...

    @abstractmethod
    async def create_schueler(self) -> int:
        ...

    @abstractmethod
    async def delete_schueler(self) -> bool:
        ...

    def __init__(self):
        self.session = database.get_session()
