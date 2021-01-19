from persistence import Schule, database

from repositories.base_repository import BaseRepository


class SchulenRepository(BaseRepository[Schule]):
    @staticmethod
    async def create(name, adresse_id) -> Schule:
        async with database.get_session() as session:
            async with session.begin():
                sch = await session.query(Schule).filter(
                    Schule.name == name,
                    Schule.adresse_id == adresse_id
                ).scalar()

                if sch is None:
                    new_schule = Schule(name, adresse_id)
                    sch = await session.add(new_schule)

                return sch
