from collections import namedtuple

import graphene


class Klasse(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    schule = graphene.Field(Schule)


class Modul(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    schule = graphene.Field(Schule)


class Firma(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    adresse = graphene.Field(Adresse)


class Person(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    vorname = graphene.String()
    adresse = graphene.Field(Adresse)


class ABV(graphene.ObjectType):
    id = graphene.ID()
    person = graphene.Field(Person)
    firma = graphene.Field(Firma)


class Schueler(graphene.ObjectType):
    id = graphene.ID()
    schueler_id = graphene.ID()
    person = graphene.Field(Person)
    firma = graphene.Field(Firma)
    abv = graphene.Field(ABV)
    klasse = graphene.Field(Klasse)
