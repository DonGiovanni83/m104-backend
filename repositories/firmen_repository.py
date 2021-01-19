import threading

from persistence import Firma, database
from repositories.base_repository import BaseRepository


class FirmenRepository(BaseRepository):
    __instance = None

    def __init__(self):
        super().__init__(Firma)
        FirmenRepository.__instance = self
        self.T = Firma

    @staticmethod
    def get_instance():
        if FirmenRepository.__instance is None:
            with threading.Lock():
                if FirmenRepository.__instance is None:
                    FirmenRepository()
        return FirmenRepository.__instance

    async def create(self, name, adresse_id) -> Firma:
        async with database.get_session() as session:
            async with session.begin():
                firma = await session.query(Firma).filter(
                    Firma.name == name,
                    Firma.adresse_id == adresse_id
                ).scalar()

                if firma is None:
                    new_firma = Firma(name, adresse_id)
                    firma = await session.add(new_firma)

                return firma
