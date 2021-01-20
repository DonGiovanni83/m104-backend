import threading

from sqlalchemy import select

from persistence import Firma, database, Adresse
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

    async def create(self, name, adresse_id):
        db_session = await database.get_session()
        async with db_session as session:
            async with session.begin():
                sch = (
                    await session.execute(
                        statement=select(Firma).where(
                            Firma.name == name,
                            Firma.adresse_id == adresse_id
                        ))
                ).first()

                if sch is None:
                    sch = Firma(
                        name=name,
                        adresse_id=adresse_id
                    )
                    session.add(sch)
                    await session.flush()
                    # reselect it with adress loaded
                    sch = (await session.execute(
                        statement=select(Firma).where(
                            Firma.id == sch.id
                        )
                    )).first()

                session.expunge_all()
                return sch[0]