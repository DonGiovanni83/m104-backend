import graphene

from api.mappers.adressen import to_gql_adresse
from api.types import Adresse
from repositories.adressen_repository import AdressenRepository


class GetAllAdressen(graphene.ObjectType):
    adressen = graphene.List(Adresse)

    async def resolve_adressen(parent, info):
        all_addr = await AdressenRepository.get_instance().get_all()
        all_gql_addr = []
        for addr in all_addr:
            all_gql_addr.append(to_gql_adresse(addr))
        return all_gql_addr


class Query(GetAllAdressen, graphene.ObjectType):
