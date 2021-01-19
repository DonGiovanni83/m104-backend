import graphene

from api.types.adresse import Adresse
from api.types.adresse.mapper import AdresseMapper
from repositories.adressen_repository import AdressenRepository


class CreateAdresseMutation(graphene.Mutation):
    class Input:
        ort: graphene.String()
        plz: graphene.Int()
        adresse_1: graphene.String()
        adresse_2: graphene.String()
        tel_g: graphene.String()
        tel_m: graphene.String()
        email_1: graphene.String()
        email_2: graphene.String()

    adresse = graphene.Field(lambda: Adresse)

    @classmethod
    async def mutate(cls, args, context, info):
        adresse = await AdressenRepository.create(
            args.get('ort', ''),
            args.get('plz', 0000),
            args.get('adresse_1', ''),
            args.get('adresse_2', ''),
            args.get('tel_g', ''),
            args.get('tel_m', ''),
            args.get('email_1', ''),
            args.get('email_2', ''),
        )

        return AdresseMapper.to_gql_adresse(adresse)
