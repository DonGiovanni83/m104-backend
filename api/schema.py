import graphene

from api.types.adresse.mutation import CreateAdresseMutation
from api.types.adresse.query import GetAllAdressen
from api.types.schule.query import GetAllSchulen


class Query(GetAllAdressen, GetAllSchulen, graphene.ObjectType):
    pass


class Mutation(CreateAdresseMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, auto_camelcase=False)
