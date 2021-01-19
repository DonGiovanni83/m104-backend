import threading

from persistence import Klasse, database
from repositories.base_repository import BaseRepository


class KlassenRepository(BaseRepository):
    __instance = None

    def __init__(self):
        super().__init__(Klasse)
        KlassenRepository.__instance = self
        self.T = Klasse

    @staticmethod
    def get_instance():
        if KlassenRepository.__instance is None:
            with threading.Lock():
                if KlassenRepository.__instance is None:
                    KlassenRepository()
        return KlassenRepository.__instance

    async def create(self, name, schule_id) -> Klasse:
        async with database.get_session() as session:
            async with session.begin():
                kl = await session.query(Klasse).filetr(
                    Klasse.name == name,
                    Klasse.schule_id == schule_id
                ).scalar()

                if kl is None:
                    new_klasse = Klasse(name, schule_id)
                    kl = await session.add(new_klasse)

            return kl
