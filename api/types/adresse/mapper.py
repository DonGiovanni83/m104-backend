from api.types.adresse import Adresse
from persistence import Adresse as DBAdresse


class AdresseMapper:

    @staticmethod
    def to_gql_adresse(db_adresse: DBAdresse) -> Adresse:
        return Adresse(
            id=db_adresse.id,
            ort=db_adresse.ort,
            plz=db_adresse.plz,
            adresse_1=db_adresse.adresse_1,
            adresse_2=db_adresse.adresse_2,
            tel_g=db_adresse.tel_g,
            tel_m=db_adresse.tel_m,
            email_1=db_adresse.email_1,
            email_2=db_adresse.email_2,
        )

    @staticmethod
    def to_gql_adresse_list(db_adr: [DBAdresse]) -> [Adresse]:
        all_gql_addr = []
        for addr in db_adr:
            all_gql_addr.append(AdresseMapper.to_gql_adresse(addr))
        return all_gql_addr
