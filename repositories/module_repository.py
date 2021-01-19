import threading

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
        async with database.get_session() as session:
            async with session.begin():
                kl = await session.query(Modul).filetr(
                    Modul.name == name,
                    Modul.schule_id == schule_id
                ).scalar()

                if kl is None:
                    new_modul = Modul(name, schule_id)
                    kl = await session.add(new_modul)

            return kl
