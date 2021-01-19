import graphene

from api.types import Adresse
from persistence import Adresse as DBAdresse


def to_gql_adresse(db_adresse: DBAdresse):
    return Adresse(
        id=graphene.ID(db_adresse.id),
        ort=graphene.String(db_adresse.ort),
        plz=graphene.String(db_adresse.plz),
        adresse_1=graphene.String(db_adresse.adresse_1),
        adresse_2=graphene.String(db_adresse.adresse_2),
        tel_g=graphene.String(db_adresse.tel_g),
        tel_m=graphene.String(db_adresse.tel_m),
        email_1=graphene.String(db_adresse.email_1),
        email_2=graphene.String(db_adresse.email_2),
    )
