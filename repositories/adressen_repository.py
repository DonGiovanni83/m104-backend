from persistence import Adresse
from repositories.base_repository import BaseRepository


class AdressenRepository(BaseRepository[Adresse]):
    async def create(self, adresse) -> Adresse:
        async with self.async_session as session:
            async with session.begin():
                addr = await session.query(Adresse).filter(
                    Adresse.ort == adresse.ort,
                    Adresse.plz == adresse.plz,
                    Adresse.adresse_1 == adresse.adresse_1,
                    Adresse.adresse_2 == adresse.adresse_2,
                    Adresse.tel_g == adresse.tel_g,
                    Adresse.tel_m == adresse.tel_m,
                    Adresse.email_1 == adresse.email_1,
                    Adresse.email_2 == adresse.email_2
                ).scalar()

                if addr is None:
                    addr = await session.add(adresse)

                return addr
