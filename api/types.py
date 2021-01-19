import graphene


class Schueler(graphene.ObjectType):
    id = graphene.ID()
    schueler_id = graphene.ID()
    person = graphene.Field(Person)
    firma = graphene.Field(Firma)
    abv = graphene.Field(ABV)
    klasse = graphene.Field(Klasse)
