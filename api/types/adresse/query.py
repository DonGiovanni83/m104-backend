import graphene

from api.types.adresse import Adresse
from api.types.adresse.mapper import AdresseMapper
from repositories.adressen_repository import AdressenRepository


class GetAllAdressen(graphene.ObjectType):
    adressen = graphene.List(Adresse)

    async def resolve_adressen(parent, info):
        all_addr = await AdressenRepository.get_instance().get_all()
        return AdresseMapper.to_gql_adresse_list(all_addr)
