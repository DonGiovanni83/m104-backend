import graphene

from api.types.schueler import Schueler
from api.types.schueler.mapper import SchuelerMapper
from repositories.schueler_repository import SchuelerRepository


class CreateSchuelerMutation(graphene.Mutation):
    class Input:
        person_id = graphene.ID()
        schueler_id = graphene.ID()
        firma_id = graphene.ID()
        abv_id = graphene.ID()
        klasse_id = graphene.ID()

    create_Schueler = graphene.Field(lambda: Schueler)

    @classmethod
    async def mutate(cls, args, context, info):
        schueler = await SchuelerRepository.get_instance().create(
            args.get('person_id', 0),
            args.get('schueler_id', 0),
            args.get('firma_id', 0),
            args.get('abv_id', 0),
            args.get('klasse_id', 0)
        )

        return SchuelerMapper.to_gql_schueler(schueler)
