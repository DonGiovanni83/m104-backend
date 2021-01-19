import graphene

from api.types.abv import ABV
from api.types.firma import Firma
from api.types.klasse import Klasse
from api.types.person import Person


class Schueler(graphene.ObjectType):
    person = graphene.Field(Person)
    schueler_id = graphene.ID()
    firma = graphene.Field(Firma)
    abv = graphene.Field(ABV)
    klasse = graphene.Field(Klasse)
