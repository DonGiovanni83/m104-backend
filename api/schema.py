import graphene

from api.mutations import Mutation
from api.query import Query

schema = graphene.Schema(query=Query, auto_camelcase=False)
