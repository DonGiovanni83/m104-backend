import graphene
from repositories.personen_repository import PersonenRepository

from api.types.person import Person
from api.types.person.mapper import PersonMapper


class GetAllPersonen(graphene.ObjectType):
    personen = graphene.List(Person)

    @classmethod
    async def resolve_personen(cls, parent, info):
        all_kl = await PersonenRepository.get_instance().get_all()
        return PersonMapper.to_gql_person_list(all_kl)
