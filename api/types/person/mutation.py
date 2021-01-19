import graphene

from api.types.person import Person
from api.types.person.mapper import PersonMapper
from repositories.personen_repository import PersonenRepository


class CreatePersonMutation(graphene.Mutation):
    class Input:
        name = graphene.String()
        vorname = graphene.String()
        adresse_id = graphene.ID()

    person = graphene.Field(lambda: Person)

    @classmethod
    async def mutate(cls, args, context, info):
        person = await PersonenRepository.create(
            args.get('name', ''),
            args.get('vorname', ''),
            args.get('adresse_id', 0000)
        )

        return PersonMapper.to_gql_person(person)
