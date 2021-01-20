import threading

from sqlalchemy import select

from persistence import Adresse, database
from repositories.base_repository import BaseRepository


class AdressenRepository(BaseRepository):
    __instance = None

    def __init__(self):
        super().__init__(Adresse)
        AdressenRepository.__instance = self
        self.T = Adresse

    @staticmethod
    def get_instance():
        if AdressenRepository.__instance is None:
            with threading.Lock():
                if AdressenRepository.__instance is None:
                    AdressenRepository()
        return AdressenRepository.__instance

    async def create(self, ort, plz, adresse_1, adresse_2, tel_g, tel_m, email_1, email_2) -> Adresse:
        db_session = await database.get_session()
        async with db_session as session:
            async with session.begin():
                addr = (await session.execute(statement=select(Adresse).where(
                    Adresse.ort == ort,
                    Adresse.plz == plz,
                    Adresse.adresse_1 == adresse_1,
                    Adresse.adresse_2 == adresse_2,
                    Adresse.tel_g == tel_g,
                    Adresse.tel_m == tel_m,
                    Adresse.email_1 == email_1,
                    Adresse.email_2 == email_2
                ))).first()

                if addr is None:
                    addr = Adresse(
                        ort=ort,
                        plz=plz,
                        adresse_1=adresse_1,
                        adresse_2=adresse_2,
                        tel_g=tel_g,
                        tel_m=tel_m,
                        email_1=email_1,
                        email_2=email_2
                    )
                    session.add(addr)
                    await session.commit()
                session.expunge_all()
                return addr[0]
