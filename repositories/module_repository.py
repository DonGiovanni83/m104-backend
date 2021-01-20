import threading

from sqlalchemy import select

from persistence import Modul, database
from repositories.base_repository import BaseRepository


class ModuleRepository(BaseRepository):
    __instance = None

    def __init__(self):
        super().__init__(Modul)
        ModuleRepository.__instance = self
        self.T = Modul

    @staticmethod
    def get_instance():
        if ModuleRepository.__instance is None:
            with threading.Lock():
                if ModuleRepository.__instance is None:
                    ModuleRepository()
        return ModuleRepository.__instance

    async def create(self, name, schule_id) -> Modul:
        db_session = await database.get_session()
        async with db_session as session:
            async with session.begin():
                md = await session.execute(statement=select(Modul).where(
                    Modul.name == name and
                    Modul.schule_id == schule_id
                ).first())

                if md is None:
                    md = Modul(name=name, schule_id=schule_id)
                    session.add(md)
                    await session.flush()

            return md[0]
