import graphene

from graphene_django import DjangoObjectType 
from .models import Programmer 

# class GreetQuery(graphene.ObjectType):
#     hello = graphene.String(default_value="Hi!")


class ProgrammerDetails(DjangoObjectType): 
    class Meta:
        model = Programmer
        fields = "__all__"


class Query(graphene.ObjectType):
    all_programmers = graphene.List(ProgrammerDetails)
    programmer = graphene.Field(ProgrammerDetails, programmer_id=graphene.Int())

    def resolve_all_programmers(self, info, **kwargs):
        return Programmer.objects.all()

    def resolve_programmer(self, info, programmer_id):
        return Programmer.objects.get(pk=programmer_id)

schema = graphene.Schema(query=Query)