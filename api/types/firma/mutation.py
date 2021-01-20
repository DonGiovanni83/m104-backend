import graphene
from graphene import InputObjectType

from api.types.firma import Firma
from api.types.firma.mapper import FirmaMapper
from repositories.adressen_repository import AdressenRepository
from repositories.firmen_repository import FirmenRepository


class CreateFirmaInput(InputObjectType):
    name = graphene.String()
    ort = graphene.String()
    plz = graphene.Int()
    adresse_1 = graphene.String()
    adresse_2 = graphene.String()
    tel_g = graphene.String()
    tel_m = graphene.String()
    email_1 = graphene.String()
    email_2 = graphene.String()


class CreateFirmaMutation(graphene.Mutation):
    class Arguments:
        input_args = CreateFirmaInput()

    ok = graphene.Boolean()
    firma = graphene.Field(Firma)

    @classmethod
    async def mutate(cls, context, info, input_args: CreateFirmaInput):
        """
        Creates a Firma entity. If adress did not exist it is also created.
        Behaviour is idempotent.
        :param context:
        :param info:
        :param input_args:
        :return:
        """
        db_adresse = await AdressenRepository.get_instance().create(
            input_args.ort,
            input_args.plz,
            input_args.adresse_1,
            input_args.adresse_2,
            input_args.tel_g,
            input_args.tel_m,
            input_args.email_1,
            input_args.email_2
        )

        db_firma = await FirmenRepository.get_instance().create(
            input_args.name,
            db_adresse.id
        )
        gql_firma = FirmaMapper.to_gql_firma(db_firma)
        return CreateFirmaMutation(firma=gql_firma, ok=True)
