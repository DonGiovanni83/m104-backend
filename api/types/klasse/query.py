import graphene

from api.types.klasse import Klasse
from api.types.klasse.mapper import KlasseMapper
from repositories.klassen_repository import KlassenRepository


class GetAllKlassen(graphene.ObjectType):
    klassen = graphene.List(Klasse)

    @classmethod
    async def resolve_klassen(cls, parent, info):
        all_kl = await KlassenRepository.get_instance().get_all()
        return KlasseMapper.to_gql_klasse_list(all_kl)
