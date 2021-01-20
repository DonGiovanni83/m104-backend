import graphene

from api.types.modul import Modul
from api.types.modul.mapper import ModulMapper
from repositories.module_repository import ModuleRepository


class CreateModulMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        schule_id = graphene.ID()

    ok = graphene.Boolean()
    modul = graphene.Field(Modul)

    @classmethod
    async def mutate(cls, context, info, name, schule_id):
        db_modul = await ModuleRepository.get_instance().create(name, schule_id)
        gql_modul = ModulMapper.to_gql_modul(db_modul)
        return CreateModulMutation(modul=gql_modul, ok=True)
