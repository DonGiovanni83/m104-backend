from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List

from persistence import database
from persistence.NotFoundException import NotFoundException

T = TypeVar('T')


class BaseRepository(Generic[T], ABC):
    """
    Generic repository with basic crud calls, which are the same for
    all entities.
    """
    def __init__(self):
        self.async_session = database.get_session()

    async def get_all(self) -> List[T]:
        async with self.async_session as session:
            async with session.begin():
                all_entities = await session.query(T).all()
                return all_entities

    async def find(self, entity_id) -> T:
        async with self.async_session as session:
            async with session.begin():
                entity = await session.query(T).filetr(T.id == entity_id).scalar()
                if entity is None:
                    raise NotFoundException()
                return entity

    @abstractmethod
    async def create(self, new_entity) -> T:
        ...

    async def delete(self, entity_id) -> bool:
        async with self.async_session as session:
            async with session.begin():
                await session.delete(T).where(T.id == entity_id)
            return True
