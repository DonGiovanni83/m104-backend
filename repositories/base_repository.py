import threading
from abc import ABC, abstractmethod
from typing import List

from sqlalchemy import select

from persistence import database
from persistence.NotFoundException import NotFoundException


class BaseRepository(ABC):
    """
    Generic repository with basic crud calls, which are the same for
    all entities.
    """

    __instance = None
    T = None

    async def get_all(self) -> List[T]:
        db_session = await database.get_session()
        async with db_session as session:
            async with session.begin():
                all_entities = await session.execute(statement=select(self.T))
                session.expunge_all()
                return all_entities

    async def find(self, entity_id) -> T:
        db_session = await database.get_session()
        async with db_session as session:
            async with session.begin():
                entity = (await session.execute(statement=select(self.T).where(self.T.id == entity_id))).first()
                if entity is None:
                    raise NotFoundException()
                return entity[0]

    @abstractmethod
    async def create(self, *args) -> T:
        ...

    async def delete(self, entity_id) -> bool:
        async with database.get_session() as session:
            async with session.begin():
                await session.delete(self.T).where(self.T.id == entity_id)
            return True

    @staticmethod
    @abstractmethod
    def get_instance():
        ...

    def __init__(self, t):
        self.T = t
