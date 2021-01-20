import threading

from sqlalchemy import select

from persistence import Schule, database, Adresse
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

    async def create(self, name, adresse_id):
        db_session = await database.get_session()
        async with db_session as session:
            async with session.begin():
                sch = (
                    await session.execute(
                        statement=select(Schule).where(
                            Schule.name == name,
                            Schule.adresse_id == adresse_id
                        ))
                ).first()

                if sch is None:
                    sch = Schule(
                        name=name,
                        adresse_id=adresse_id
                    )
                    session.add(sch)
                    await session.flush()
                    # reselect it with adress loaded
                    sch = (await session.execute(
                        statement=select(Schule).where(
                            Schule.id == sch.id
                        )
                    )).first()

                session.expunge_all()

                return sch[0]

    async def get_all(self):
        db_session = await database.get_session()
        async with db_session as session:
            async with session.begin():
                all_schulen = await session.execute(statement=select(Schule).join(Adresse))
                session.expunge_all()
                return all_schulen
