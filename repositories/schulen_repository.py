from persistence import Schule

from repositories.base_repository import BaseRepository, T


class SchulenRepository(BaseRepository[Schule]):
    async def create(self, schule) -> Schule:
        async with self.async_session as session:
            async with session.begin():
                sch = await session.query(Schule).filter(
                    Schule.name == schule.name,
                    Schule.adresse_id == schule.adresse_id
                ).scalar()

                if sch is None:
                    sch = await session.add(schule)

                return sch
