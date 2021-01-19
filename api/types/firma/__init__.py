import graphene

from api.types.adresse import Adresse


class Firma(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    adresse = graphene.Field(Adresse)
