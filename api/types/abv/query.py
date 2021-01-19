import graphene

from api.types.abv import ABV
from api.types.abv.mapper import ABVMapper
from repositories.abvs_repository import ABVsRepository


class GetAllABVs(graphene.ObjectType):
    abvs = graphene.List(ABV)

    @classmethod
    async def resolve_abvs(cls, parent, info):
        all_abvs = await ABVsRepository.get_instance().get_all()
        return ABVMapper.to_gql_abv_list(all_abvs)
