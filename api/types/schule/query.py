import graphene

from api.types.schule import Schule
from api.types.schule.mapper import SchuleMapper
from repositories.schulen_repository import SchulenRepository


class GetAllSchulen(graphene.ObjectType):
    schulen = graphene.List(Schule)

    @staticmethod
    async def resolve_schulen(parent, info):
        all_sch = await SchulenRepository.get_instance().get_all()
        return SchuleMapper.to_gql_schule_list(all_sch)
