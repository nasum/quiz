from graphene_django import DjangoObjectType
from modules.questions.models import Answers


class AnswersType(DjangoObjectType):
    class Meta:
        model = Answers
