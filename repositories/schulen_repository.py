import threading

from persistence import Schule, database
from repositories.base_repository import BaseRepository


class SchulenRepository(BaseRepository):
    __instance = None

    def __init__(self):
        super().__init__(Schule)
        SchulenRepository.__instance = self
        self.T = Schule

    @staticmethod
    def get_instance():
        if SchulenRepository.__instance is None:
            with threading.Lock():
                if SchulenRepository.__instance is None:
                    SchulenRepository()
        return SchulenRepository.__instance

    async def create(self, name, adresse_id) -> Schule:
        async with database.get_session() as session:
            async with session.begin():
                sch = await session.query(Schule).filter(
                    Schule.name == name,
                    Schule.adresse_id == adresse_id
                ).scalar()

                if sch is None:
                    new_schule = Schule(name, adresse_id)
                    sch = await session.add(new_schule)

                return sch
