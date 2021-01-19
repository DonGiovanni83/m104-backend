from api.types.firma import Firma
from persistence import Firma as DBFirma


class FirmaMapper:
    @staticmethod
    def to_gql_firma(db_firma: DBFirma) -> Firma:
        return Firma(
            id=db_firma.id,
            name=db_firma.name,
            adresse_id=db_firma.adresse_id
        )

    @staticmethod
    def to_gql_firma_list(db_firmen: [DBFirma]) -> [Firma]:
        all_gql_firmen = []
        for sch in db_firmen:
            all_gql_firmen.append(FirmaMapper.to_gql_firma(sch))

        return all_gql_firmen
