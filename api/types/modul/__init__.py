import graphene

from api.types.schule import Schule


class Modul(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    schule = graphene.Field(Schule)
