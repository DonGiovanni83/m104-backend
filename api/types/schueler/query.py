import graphene

from api.types.schueler import Schueler
from api.types.schueler.mapper import SchuelerMapper
from repositories.schueler_repository import SchuelerRepository


class GetAllSchueler(graphene.ObjectType):
    schueler = graphene.List(Schueler)

    @classmethod
    async def resolve_schueler(cls, parent, info):
        all_schueler = await SchuelerRepository.get_instance().get_all()
        return SchuelerMapper.to_gql_schueler_list(all_schueler)
