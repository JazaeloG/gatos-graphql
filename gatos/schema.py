import graphene
from graphene_django import DjangoObjectType
from .models import *

class GatoType(DjangoObjectType):
    class Meta:
        model = Gato


class Query(graphene.ObjectType):
    gatos = graphene.List(GatoType)

    
    def resolve_gatos(self, info, **kwargs):
        return Gato.objects.all()
    


