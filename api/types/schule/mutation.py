import graphene

from api.types.schule import Schule
from api.types.schule.mapper import SchuleMapper
from repositories.schulen_repository import SchulenRepository


class CreateSchuleMutation(graphene.Mutation):
    class Input:
        name: graphene.String()
        adresse_id: graphene.ID()

    schule = graphene.Field(lambda: Schule)

    @classmethod
    async def mutate(cls, args, context, info):
        schule = await SchulenRepository.create(
            args.get('name', ''),
            args.get('adresse_id', 0000)
        )

        return SchuleMapper.to_gql_schule(schule)
