import threading

from persistence import ABV, database
from repositories.base_repository import BaseRepository


class ABVsRepository(BaseRepository):
    __instance = None

    def __init__(self):
        super().__init__(ABV)
        ABVsRepository.__instance = self
        self.T = ABV

    @staticmethod
    def get_instance():
        if ABVsRepository.__instance is None:
            with threading.Lock():
                if ABVsRepository.__instance is None:
                    ABVsRepository()
        return ABVsRepository.__instance

    async def create(self, name, person_id, firma_id) -> ABV:
        async with database.get_session() as session:
            async with session.begin():
                abv = await session.query(ABV).filter(
                    ABV.id == person_id,
                    ABV.firmen_id == firma_id
                ).scalar()

                if abv is None:
                    new_abv = ABV( person_id, firma_id)
                    abv = await session.add(new_abv)

                return abv
