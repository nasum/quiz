from graphene_django import DjangoObjectType
from modules.questions.models import Questions

class QuestionsType(DjangoObjectType):
    class Meta:
        model = Questions