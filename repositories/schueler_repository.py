import threading

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
        async with database.get_session() as session:
            async with session.begin():
                schueler = await session.query(Schueler).filter(
                    # should already be a primary key and therefore unique
                    Schueler.schueler_id == schueler_id
                ).scalar()

                if schueler is None:
                    new_schueler = Schueler(
                        person_id,
                        schueler_id,
                        firma_id,
                        abv_id,
                        klasse_id
                    )
                    schueler = await session.add(new_schueler)

                return schueler
