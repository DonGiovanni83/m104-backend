import graphene

from api.types.modul import Modul
from api.types.modul.mapper import ModulMapper
from repositories.module_repository import ModuleRepository


class CreateModulMutation(graphene.Mutation):
    class Input:
        name: graphene.String()
        schule_id: graphene.ID()

    modul = graphene.Field(lambda: Modul)

    @classmethod
    async def mutate(cls, args, context, info):
        modul = await ModuleRepository.create(
            args.get('name', ''),
            args.get('schule_id', 0000)
        )

        return ModulMapper.to_gql_modul(modul)
