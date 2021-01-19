from api.types.abv import ABV
from persistence import ABV as DBABV


class ABVMapper:
    @staticmethod
    def to_gql_abv(db_abv: DBABV) -> ABV:
        return ABV(
            person_id=db_abv.id,
            firma_id=db_abv.firmen_id,
        )

    @staticmethod
    def to_gql_abv_list(db_abvs: [DBABV]) -> [ABV]:
        all_gql_abvs = []
        for abv in db_abvs:
            all_gql_abvs.append(ABVMapper.to_gql_abv(abv))

        return all_gql_abvs
