import threading

from sqlalchemy import select

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

    async def create(self, person_id, firma_id) -> ABV:
        db_session = await database.get_session()
        async with db_session as session:
            async with session.begin():
                # TODO Fix create logic. makes no sense like that
                abv = (await session.execute(statement=select(ABV).where(
                    ABV.id == person_id,
                    ABV.firmen_id == firma_id
                ))).first()

                if abv is None:
                    abv = ABV(person_id=person_id, firma_id=firma_id)
                    session.add(abv)
                    await session.flush()

                session.expunge_all()
                return abv[0]
