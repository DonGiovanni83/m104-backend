import graphene

from api.types.modul import Modul
from api.types.modul.mapper import ModulMapper
from repositories.module_repository import ModuleRepository


class CreateModulMutation(graphene.Mutation):
    class Input:
        name: graphene.String()
        schule_id: graphene.ID()

    create_modul = graphene.Field(lambda: Modul)

    @classmethod
    async def mutate(cls, args, context, info):
        modul = await ModuleRepository.get_instance().create(
            args.get('name', ''),
            args.get('schule_id', 0)
        )

        return ModulMapper.to_gql_modul(modul)
