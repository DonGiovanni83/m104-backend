import graphene

from api.types.abv.query import GetAllABVs
from api.types.adresse.mutation import CreateAdresseMutation
from api.types.adresse.query import GetAllAdressen
from api.types.firma.query import GetAllFirmen
from api.types.klasse.mutation import CreateKlasseMutation
from api.types.klasse.query import GetAllKlassen
from api.types.modul.mutation import CreateModulMutation
from api.types.modul.query import GetAllModule
from api.types.person.query import GetAllPersonen
from api.types.schueler.query import GetAllSchueler
from api.types.schule.mutation import CreateSchuleMutation
from api.types.schule.query import GetAllSchulen


class Query(
    GetAllAdressen,
    GetAllSchulen,
    GetAllKlassen,
    GetAllModule,
    GetAllFirmen,
    GetAllPersonen,
    GetAllABVs,
    GetAllSchueler,
    graphene.ObjectType
):
    pass


class Mutation(graphene.ObjectType):
    create_adresse = CreateAdresseMutation.Field()
    create_schule = CreateSchuleMutation.Field()
    create_klasse = CreateKlasseMutation.Field()
    create_modul = CreateModulMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation, auto_camelcase=False)
