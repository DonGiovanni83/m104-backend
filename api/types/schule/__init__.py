import graphene

from api.types.adresse import Adresse


class Schule(graphene.ObjectType):
    s_id = graphene.ID()
    name = graphene.String()
    adresse = graphene.Field(Adresse)
