import graphene


class Adresse(graphene.ObjectType):
    id = graphene.ID()
    ort = graphene.String()
    plz = graphene.Int()
    adresse_1 = graphene.String()
    adresse_2 = graphene.String()
    tel_g = graphene.String()
    tel_m = graphene.String()
    email_1 = graphene.String()
    email_2 = graphene.String()
