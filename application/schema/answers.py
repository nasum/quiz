import graphene
from graphene_django import DjangoObjectType
from modules.questions.models import Answers


class AnswersType(DjangoObjectType):
    class Meta:
        model = Answers
    description = graphene.String()
    right = graphene.Boolean()


class AnswersInputType(graphene.InputObjectType):
    description = graphene.String(require=True)
    right = graphene.Boolean()