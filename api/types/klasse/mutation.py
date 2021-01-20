import graphene

from api.types.klasse import Klasse
from api.types.klasse.mapper import KlasseMapper
from repositories.klassen_repository import KlassenRepository


class CreateKlasseMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        schule_id = graphene.ID()

    ok = graphene.Boolean()
    klasse = graphene.Field(Klasse)

    @classmethod
    async def mutate(cls, context, info, name, schule_id):
        db_klasse = await KlassenRepository.get_instance().create(name, schule_id)
        gql_klasse = KlasseMapper.to_gql_klasse(db_klasse)
        return CreateKlasseMutation(klasse=gql_klasse, ok=True)
