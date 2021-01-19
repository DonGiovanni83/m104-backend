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

    @staticmethod
    async def get_all() -> List[T]:
        async with database.get_session() as session:
            async with session.begin():
                all_entities = await session.query(T).all()
                return all_entities

    @staticmethod
    async def find(entity_id) -> T:
        async with database.get_session() as session:
            async with session.begin():
                entity = await session.query(T).filetr(T.id == entity_id).scalar()
                if entity is None:
                    raise NotFoundException()
                return entity

    @staticmethod
    @abstractmethod
    async def create(*args) -> T:
        ...

    @staticmethod
    async def delete(entity_id) -> bool:
        async with database.get_session() as session:
            async with session.begin():
                await session.delete(T).where(T.id == entity_id)
            return True
