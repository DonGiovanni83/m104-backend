import graphene

from api.types.adresse.mutation import CreateAdresseMutation
from api.types.adresse.query import GetAllAdressen
from api.types.firma.query import GetAllFirmen
from api.types.klasse.query import GetAllKlassen
from api.types.modul.query import GetAllModule
from api.types.person.query import GetAllPersonen
from api.types.schule.query import GetAllSchulen


class Query(
    GetAllAdressen,
    GetAllSchulen,
    GetAllKlassen,
    GetAllModule,
    GetAllFirmen,
    GetAllPersonen,
    graphene.ObjectType
):
    pass


class Mutation(CreateAdresseMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, auto_camelcase=False)
