import threading

from sqlalchemy import select

from persistence import Person, database
from repositories.base_repository import BaseRepository


class PersonenRepository(BaseRepository):
    __instance = None

    def __init__(self):
        super().__init__(Person)
        PersonenRepository.__instance = self
        self.T = Person

    @staticmethod
    def get_instance():
        if PersonenRepository.__instance is None:
            with threading.Lock():
                if PersonenRepository.__instance is None:
                    PersonenRepository()
        return PersonenRepository.__instance

    async def create(self, name, vorname, adresse_id) -> Person:
        db_session = await database.get_session()
        async with db_session as session:
            async with session.begin():
                prs = (await session.execute(statement=select(Person).where(
                    Person.name == name,
                    Person.vorname == vorname,
                    Person.adresse_id == adresse_id
                ))).first()

                if prs is None:
                    prs = Person(name=name, vorname=vorname, adresse_id=adresse_id)
                    session.add(prs)
                    await session.flush()

                return prs[0]
