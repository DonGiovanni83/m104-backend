import graphene

from api.types.abv import ABV
from api.types.abv.mapper import ABVMapper
from repositories.abvs_repository import ABVsRepository


class CreateABVMutation(graphene.Mutation):
    class Input:
        person_id = graphene.ID()
        firma_id = graphene.ID()

    create_abv = graphene.Field(lambda: ABV)

    @classmethod
    async def mutate(cls, args, context, info):
        abv = await ABVsRepository.get_instance().create(
            args.get('person_id', 0),
            args.get('firma_id', 0)
        )

        return ABVMapper.to_gql_abv(abv)
