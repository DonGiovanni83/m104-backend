from api.types.schule import Schule
from persistence import Schule as DBSchule


class SchuleMapper:
    @staticmethod
    def to_gql_schule(db_schule: DBSchule) -> Schule:
        return Schule(
            id=db_schule.id,
            name=db_schule.name,
            adresse_id=db_schule.adresse_id
        )

    @staticmethod
    def to_gql_schule_list(db_schulen: [DBSchule]) -> [Schule]:
        all_gql_schulen = []
        for sch in db_schulen:
            all_gql_schulen.append(SchuleMapper.to_gql_schule(sch))

        return all_gql_schulen
