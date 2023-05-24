import graphene
from gatos import schema



class Query(schema.Query, graphene.ObjectType):
    pass




schema = graphene.Schema(query=Query)