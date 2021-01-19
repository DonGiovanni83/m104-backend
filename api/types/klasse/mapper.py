from api.types.klasse import Klasse
from persistence import Klasse as DBKlasse


class KlasseMapper:
    @staticmethod
    def to_gql_klasse(db_klasse: DBKlasse) -> Klasse:
        return Klasse(
            id=db_klasse.id,
            name=db_klasse.name,
            schule_id=db_klasse.schule_id
        )

    @staticmethod
    def to_gql_klasse_list(db_klassen: [DBKlasse]) -> [Klasse]:
        all_gql_klassen = []
        for sch in db_klassen:
            all_gql_klassen.append(KlasseMapper.to_gql_klasse(sch))

        return all_gql_klassen
