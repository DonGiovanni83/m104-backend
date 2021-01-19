from persistence import Klasse, database
from repositories.base_repository import BaseRepository


class KlassenRepository(BaseRepository[Klasse]):

    @staticmethod
    async def create(name, schule_id) -> Klasse:
        async with database.get_session() as session:
            async with session.begin():
                kl = await session.query(Klasse).filetr(
                    Klasse.name == name,
                    Klasse.schule_id == schule_id
                ).scalar()

                if kl is None:
                    new_klasse = Klasse(name, schule_id)
                    kl = await session.add(new_klasse)

            return kl
