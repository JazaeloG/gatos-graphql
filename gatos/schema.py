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
    


class CreateGato(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    image = graphene.String()
    ataque = graphene.Int()
    defensa = graphene.Int()
    tipo = graphene.String()
    counter = graphene.String()
    strong = graphene.String()

    #2
    class Arguments:
        name = graphene.String()
        image = graphene.String()
        ataque = graphene.Int()
        defensa = graphene.Int()
        tipo = graphene.String()
        counter = graphene.String()
        strong = graphene.String()

    #3
    def mutate(self, info, name, image,ataque,defensa,counter,strong,tipo):
        gato = Gato(name=name, image=image,ataque=ataque,strong=strong,counter=counter,defensa=defensa,tipo=tipo)
        gato.save()

        return CreateGato(
            id =gato.id,
            name=gato.name,
            tipo=gato.tipo,
            ataque=gato.ataque,
            counter=gato.counter,
            defensa=gato.defensa,
            image=gato.image,
            strong=gato.strong
        )


#4
class Mutation(graphene.ObjectType):
    create_gato = CreateGato.Field()