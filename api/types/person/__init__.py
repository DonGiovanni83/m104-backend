import graphene

from api.types.adresse import Adresse


class Person(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    vorname = graphene.String()
    adresse = graphene.Field(Adresse)
