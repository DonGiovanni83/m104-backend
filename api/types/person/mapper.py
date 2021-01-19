from api.types.person import Person
from persistence import Person as DBPerson


class PersonMapper:
    @staticmethod
    def to_gql_person(db_person: DBPerson) -> Person:
        return Person(
            id=db_person.id,
            name=db_person.name,
            vorname=db_person.vorname,
            adresse_id=db_person.adresse_id
        )

    @staticmethod
    def to_gql_person_list(db_personen: [DBPerson]) -> [Person]:
        all_gql_personen = []
        for prs in db_personen:
            all_gql_personen.append(PersonMapper.to_gql_person(prs))

        return all_gql_personen
