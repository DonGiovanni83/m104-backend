import graphene
from repositories.firmen_repository import FirmenRepository

from api.types.firma import Firma
from api.types.firma.mapper import FirmaMapper


class GetAllFirmen(graphene.ObjectType):
    firmen = graphene.List(Firma)

    @classmethod
    async def resolve_firmen(cls, parent, info):
        all_kl = await FirmenRepository.get_instance().get_all()
        return FirmaMapper.to_gql_firma_list(all_kl)
