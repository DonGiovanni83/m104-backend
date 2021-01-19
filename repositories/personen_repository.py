import threading

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
        async with database.get_session() as session:
            async with session.begin():
                prs = await session.query(Person).filter(
                    Person.name == name,
                    Person.vorname == vorname,
                    Person.adresse_id == adresse_id
                ).scalar()

                if prs is None:
                    new_person = Person(name, vorname, adresse_id)
                    sch = await session.add(new_person)

                return sch
