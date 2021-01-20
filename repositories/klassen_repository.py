import threading

from sqlalchemy import select

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

    async def create(self, name, schule_id):
        db_session = await database.get_session()
        async with db_session as session:
            async with session.begin():
                kl = (await session.execute(statement=select(Klasse).where(
                    Klasse.name == name,
                    Klasse.schule_id == schule_id
                ))).first()

                if kl is None:
                    kl = Klasse(name=name, schule_id=schule_id)
                    session.add(kl)
                    await session.flush()
                    # reselect everything so fields are loaded
                    kl = (await session.execute(
                        statement=select(Klasse).where(
                            Klasse.id == kl.id
                        )
                    )).first()

                session.expunge_all()
                return kl[0]
