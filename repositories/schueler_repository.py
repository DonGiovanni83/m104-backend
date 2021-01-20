import threading

from sqlalchemy import select

from persistence import database, Schueler
from repositories.base_repository import BaseRepository


class SchuelerRepository(BaseRepository):
    __instance = None

    def __init__(self):
        super().__init__(Schueler)
        SchuelerRepository.__instance = self
        self.T = Schueler

    @staticmethod
    def get_instance():
        if SchuelerRepository.__instance is None:
            with threading.Lock():
                if SchuelerRepository.__instance is None:
                    SchuelerRepository()
        return SchuelerRepository.__instance

    async def create(self, person_id, schueler_id, firma_id, abv_id, klasse_id) -> Schueler:
        db_session = await database.get_session()
        async with db_session as session:
            async with session.begin():
                schueler = (await session.execute(statement=select(Schueler).where(
                    # should already be a primary key and therefore unique
                    Schueler.schueler_id == schueler_id
                ))).first()

                if schueler is None:
                    schueler = Schueler(
                        person_id,
                        schueler_id,
                        firma_id,
                        abv_id,
                        klasse_id
                    )
                    session.add(schueler)
                    await session.flush()

                return schueler[0]
