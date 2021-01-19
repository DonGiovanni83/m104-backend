from persistence import Adresse
from repositories.base_repository import BaseRepository


class AdressenRepository(BaseRepository[Adresse]):
    async def create(self, ort, plz, addr_1, addr_2, tel_g, tel_m, email_1, email_2) -> Adresse:
        async with self.async_session as session:
            async with session.begin():
                addr = await session.query(Adresse).filter(
                    Adresse.ort == ort,
                    Adresse.plz == plz,
                    Adresse.adresse_1 == addr_1,
                    Adresse.adresse_2 == addr_2,
                    Adresse.tel_g == tel_g,
                    Adresse.tel_m == tel_m,
                    Adresse.email_1 == email_1,
                    Adresse.email_2 == email_2
                ).scalar()

                if addr is None:
                    new_addr = Adresse(ort, plz, addr_1, addr_2, tel_g, tel_m, email_1, email_2)
                    addr = await session.add(new_addr)

                return addr
