import graphene
from graphene import InputObjectType

from api.types.adresse import Adresse
from api.types.adresse.mapper import AdresseMapper
from repositories.adressen_repository import AdressenRepository


class CreateAdresseInput(InputObjectType):
    ort = graphene.String()
    plz = graphene.Int()
    adresse_1 = graphene.String()
    adresse_2 = graphene.String()
    tel_g = graphene.String()
    tel_m = graphene.String()
    email_1 = graphene.String()
    email_2 = graphene.String()


class CreateAdresseMutation(graphene.Mutation):
    class Arguments:
        input_args = CreateAdresseInput()

    ok = graphene.Boolean()
    adresse = graphene.Field(lambda: Adresse)

    @classmethod
    async def mutate(cls, context, info, input_args: CreateAdresseInput):
        adresse = await AdressenRepository.get_instance().create(
            input_args.ort,
            input_args.plz,
            input_args.adresse_1,
            input_args.adresse_2,
            input_args.tel_g,
            input_args.tel_m,
            input_args.email_1,
            input_args.email_2
        )

        adresse = AdresseMapper.to_gql_adresse(adresse)
            
        return CreateAdresseMutation(adresse=adresse, ok=True)
