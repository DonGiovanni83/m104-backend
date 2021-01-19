import graphene

from api.types.schule import Schule
from api.types.schule.mapper import SchuleMapper
from repositories.schulen_repository import SchulenRepository


class GetAllSchulen(graphene.ObjectType):
    schulen = graphene.List(Schule)

    @classmethod
    async def resolve_schulen(cls, parent, info):
        all_sch = await SchulenRepository.get_instance().get_all()
        return SchuleMapper.to_gql_schule_list(all_sch)
