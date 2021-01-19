from typing import List

from persistence.NotFoundException import NotFoundException
from persistence import Adresse
from repositories.abstract import AbstractAdressenRepository


class AdressenRepository(AbstractAdressenRepository):
    async def get_adressen(self) -> List[Adresse]:
        pass

    async def find_adresse(self, sid) -> Adresse:
        schule = await self.session.query(Adresse).filter(Adresse.id == sid).scalar()
        if schule is None:
            raise NotFoundException()

        return schule

    async def create_adresse(self, adresse) -> Adresse:
        addr = await self.session.query(Adresse).filter(
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
            addr = await self.session.add(adresse)
            await self.session.commit()
        return addr

    async def delete_adresse(self) -> bool:
        pass
