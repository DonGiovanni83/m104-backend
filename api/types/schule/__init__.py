import graphene

from api.types.adresse import Adresse


class Schule(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    adresse = graphene.Field(Adresse)

"""    @staticmethod
    async def resolve_adresse_id(parent, info, id):
        (await session.execute(statement=select(Adresse)
"""