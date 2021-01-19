from api.types.schueler import Schueler
from persistence import Schueler as DBSchueler


class SchuelerMapper:
    @staticmethod
    def to_gql_schueler(db_schueler: DBSchueler) -> Schueler:
        return Schueler(
            person_id=db_schueler.id,
            schueler_id=db_schueler.schueler_id,
            firma_id=db_schueler.firmen_id,
            abv_id=db_schueler.abv_id,
            klasse_id=db_schueler.klasse_id
        )

    @staticmethod
    def to_gql_schueler_list(db_schueler: [DBSchueler]) -> [Schueler]:
        all_gql_schueler = []
        for schueler in db_schueler:
            all_gql_schueler.append(SchuelerMapper.to_gql_schueler(schueler))

        return all_gql_schueler
