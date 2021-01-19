import graphene

from api.types.firma import Firma
from api.types.firma.mapper import FirmaMapper
from repositories.firmen_repository import FirmenRepository


class CreateFirmaMutation(graphene.Mutation):
    class Input:
        name: graphene.String()
        adresse_id: graphene.ID()

    firma = graphene.Field(lambda: Firma)

    @classmethod
    async def mutate(cls, args, context, info):
        firma = await FirmenRepository.create(
            args.get('name', ''),
            args.get('adresse_id', 0000)
        )

        return FirmaMapper.to_gql_firma(firma)
