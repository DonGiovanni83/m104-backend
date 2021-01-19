import graphene

from api.types.firma import Firma
from api.types.person import Person


class ABV(graphene.ObjectType):
    person = graphene.Field(Person)
    firma = graphene.Field(Firma)
