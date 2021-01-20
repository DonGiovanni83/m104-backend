from api.types.modul import Modul
from api.types.schule.mapper import SchuleMapper
from persistence import Modul as DBModul


class ModulMapper:
    @staticmethod
    def to_gql_modul(db_modul: DBModul) -> Modul:
        return Modul(
            id=db_modul.id,
            name=db_modul.name,
            schule=SchuleMapper.to_gql_schule(db_modul.schule)
        )

    @staticmethod
    def to_gql_modul_list(db_module: [DBModul]) -> [Modul]:
        all_gql_module = []
        for sch in db_module:
            all_gql_module.append(ModulMapper.to_gql_modul(sch[0]))

        return all_gql_module
