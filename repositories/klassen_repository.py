from persistence import Klasse
from repositories.base_repository import BaseRepository


class KlassenRepository(BaseRepository[Klasse]):

    async def create(self, klasse) -> Klasse:
        async with self.async_session as session:
            async with session.begin():
                kl = await session.query(Klasse).filetr(
                    Klasse.name == klasse.name,
                    Klasse.schule_id == klasse.schule_id
                ).scalar()

                if kl is None:
                    kl = await session.add(kl)

                return kl
