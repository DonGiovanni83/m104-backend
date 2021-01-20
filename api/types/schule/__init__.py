import graphene

from api.types.adresse import Adresse


class Schule(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    adresse = graphene.Field(Adresse)
