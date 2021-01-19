from persistence import Klasse
from repositories.base_repository import BaseRepository


class KlassenRepository(BaseRepository[Klasse]):

    async def create(self, name, schule_id) -> Klasse:
        async with self.async_session as session:
            async with session.begin():
                kl = await session.query(Klasse).filetr(
                    Klasse.name == name,
                    Klasse.schule_id == schule_id
                ).scalar()

                if kl is None:
                    new_klasse = Klasse(name, schule_id)
                    kl = await session.add(new_klasse)

            return kl
