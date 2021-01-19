from typing import List

from persistence import Schule
from persistence.NotFoundException import NotFoundException
from repositories.abstract import AbstractSchulenRepository


class SchulenRepository(AbstractSchulenRepository):
    async def get_schulen(self) -> List[Schule]:
        pass

    async def find_schule(self, sid) -> Schule:
        schule = await self.session.query(Schule).filter(Schule.id == sid).scalar()
        if schule is None:
            raise NotFoundException()

        return schule

    async def create_schule(self, schule) -> Schule:
        sch = await self.session.query(Schule).filter(
            Schule.name == schule.name,
            Schule.adresse_id == schule.adresse_id
        ).scalar()

        if schule is None:
            sch = await self.session.add(schule)
            await self.session.commit()
        return sch

    async def delete_schule(self) -> bool:
        pass