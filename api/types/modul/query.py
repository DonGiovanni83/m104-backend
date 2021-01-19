import graphene
from repositories.module_repository import ModuleRepository

from api.types.modul import Modul
from api.types.modul.mapper import ModulMapper


class GetAllModule(graphene.ObjectType):
    module = graphene.List(Modul)

    @classmethod
    async def resolve_module(cls, parent, info):
        all_kl = await ModulnRepository.get_instance().get_all()
        return ModulMapper.to_gql_modul_list(all_kl)
