from api.types.klasse import Klasse
from api.types.schule.mapper import SchuleMapper
from persistence import Klasse as DBKlasse


class KlasseMapper:
    @staticmethod
    def to_gql_klasse(db_klasse: DBKlasse) -> Klasse:
        return Klasse(
            id=db_klasse.id,
            name=db_klasse.name,
            schule=SchuleMapper.to_gql_schule(db_klasse.schule)
        )

    @staticmethod
    def to_gql_klasse_list(db_klassen: [DBKlasse]) -> [Klasse]:
        all_gql_klassen = []
        for kl in db_klassen:
            all_gql_klassen.append(KlasseMapper.to_gql_klasse(kl[0]))

        return all_gql_klassen
