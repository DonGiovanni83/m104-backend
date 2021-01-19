import strawberry

from api.data import Adresse, Klasse, Schule
from persistence import Adresse as DBAdresse, Schule as DBSchule, Klasse as DBKlasse, database
from persistence.NotFoundException import NotFoundException
from repositories.adressen_repository import AdressenRepository
from repositories.klassen_repository import KlassenRepository
from repositories.schulen_repository import SchulenRepository

ADD_CLASS_EXAMPLE = """
"""


@strawberry.input
class CreateKlasseInput:
    name: str
    schule_id: int


@strawberry.input
class CreateSchuleInput:
    name: str
    adresse_id: int


@strawberry.input
class CreateAdresseInput:
    ort: str
    plz: int
    adresse_1: str
    adresse_2: str
    tel_g: str
    tel_m: str
    email_1: str
    email_2: str


@strawberry.type
class CreatedKlasse:
    klasse: Klasse


@strawberry.type
class CreatedAdresse:
    adresse: Adresse


@strawberry.type
class CreatedSchule:
    schule: Schule


@strawberry.type
class CreateFailed:
    error: str
    suggestion: str = "Fix the error and retry"


CreateAdresseResult = strawberry.union("CreateAdresseResult", (CreatedAdresse, CreateFailed),
                                       description="Union of possible outcomes when creating an adress")
CreateSchuleResult = strawberry.union("CreateSchuleResult", (CreatedSchule, CreateFailed),
                                      description="Union of possible outcomes when creating a school")
CreateKlasseResult = strawberry.union("CreateKlasseResult", (CreatedKlasse, CreateFailed),
                                      description="Union of possible outcomes when creating a class")

schulen_repo = SchulenRepository()
adressen_repo = AdressenRepository()
klassen_repo = KlassenRepository()


@strawberry.type
class Mutation:
    @strawberry.mutation(
        description=f"Erstelle eine neue Adresse. Bsp:{ADD_CLASS_EXAMPLE}"
    )
    def create_adresse(self, input: CreateAdresseInput) -> CreateAdresseResult:
        adresse = DBAdresse(
            ort=input.ort,
            plz=input.plz,
            adresse_1=input.adresse_1,
            adresse_2=input.adresse_2,
            tel_g=input.tel_g,
            tel_m=input.tel_m,
            email_1=input.email_1,
            email_2=input.email_2
        )

        adressen_repo.create_adresse(adresse=adresse)
        return CreateAdresseResult(adresse=adresse)

    @strawberry.mutation(
        description=f"Erstelle eine neue Schule. Bsp:{ADD_CLASS_EXAMPLE}"
    )
    def create_schule(self, input: CreateSchuleInput) -> CreateSchuleResult:

        name = input.name
        adresse_id = input

        try:
            adresse = adressen_repo.find_adresse(adresse_id)

        except NotFoundException:
            return CreateFailed(
                error='Schule konne nich erfasst werden.'
            )
        schule = DBSchule(
            name=name,
            adresse=adresse
        )
        schulen_repo.create_schule(schule)

    @strawberry.mutation(
        description=f"Erstelle eine neue Klasse. Bsp:{ADD_CLASS_EXAMPLE}"
    )
    def create_klasse(self, input: CreateKlasseInput) -> CreateKlasseResult:
        name = input.name
        schule_id = input.schule_id

        try:
            schule = schulen_repo.find_schule(schule_id)
        except Exception:
            return CreateFailed(
                error=f"Could not fine schule with id = {schule_id}"
            )

        klasse = DBKlasse(name=name, schule=schule)
        klassen_repo.create_klasse(klasse=klasse)
        return CreateKlasseResult(klasse=klasse)
