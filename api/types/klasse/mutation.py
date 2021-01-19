import graphene

from api.types.klasse import Klasse
from api.types.klasse.mapper import KlasseMapper
from repositories.klassen_repository import KlassenRepository


class CreateKlasseMutation(graphene.Mutation):
    class Input:
        name: graphene.String()
        schule_id: graphene.ID()

    create_klasse = graphene.Field(lambda: Klasse)

    @classmethod
    async def mutate(cls, args, context, info):
        klasse = await KlassenRepository.create(
            args.get('name', ''),
            args.get('schule_id', 0000)
        )

        return KlasseMapper.to_gql_klasse(klasse)
