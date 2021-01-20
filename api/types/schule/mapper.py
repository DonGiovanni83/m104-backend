from api.types.adresse import Adresse
from api.types.adresse.mapper import AdresseMapper
from api.types.schule import Schule
from persistence import Schule as DBSchule


class SchuleMapper:
    @staticmethod
    def to_gql_schule(db_schule: DBSchule) -> Schule:
        return Schule(
            id=db_schule.id,
            name=db_schule.name,
            adresse=AdresseMapper.to_gql_adresse(db_schule.adresse)
        )

    @staticmethod
    def to_gql_schule_list(db_schulen: [DBSchule]) -> [Schule]:
        all_gql_schulen = []
        for sch in db_schulen:
            all_gql_schulen.append(SchuleMapper.to_gql_schule(sch[0]))

        return all_gql_schulen
