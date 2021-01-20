import graphene
from graphene import InputObjectType

from repositories.adressen_repository import AdressenRepository
from repositories.schulen_repository import SchulenRepository


class CreateSchuleInput(InputObjectType):
    name = graphene.String()
    ort = graphene.String()
    plz = graphene.Int()
    adresse_1 = graphene.String()
    adresse_2 = graphene.String()
    tel_g = graphene.String()
    tel_m = graphene.String()
    email_1 = graphene.String()
    email_2 = graphene.String()


class CreateSchuleMutation(graphene.Mutation):
    class Arguments:
        input_args = CreateSchuleInput()

    ok = graphene.Boolean()
    id = graphene.ID()

    @classmethod
    async def mutate(cls, context, info, input_args: CreateSchuleInput):
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

        db_schule = await SchulenRepository.get_instance().create(
            input_args.name,
            db_adresse.id
        )

        return CreateSchuleMutation(id=db_schule.id, ok=True)
