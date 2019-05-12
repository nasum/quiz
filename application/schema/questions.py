import graphene
from graphene_django import DjangoObjectType
from modules.questions.models import Questions
from schema.answers import AnswersInputType, AnswersType

class QuestionsType(DjangoObjectType):
    class Meta:
        model = Questions
    description = graphene.String()
    answers = graphene.List(AnswersType)


class QuestionsInputType(graphene.InputObjectType):
    description = graphene.String(require=True)
    answers = graphene.List(AnswersInputType)