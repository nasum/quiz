import graphene
from graphene_django import DjangoObjectType
from modules.questions.models import Answers, Questions, Terms
from schema.answers import AnswersType
from schema.questions import QuestionsType
from schema.terms import CreateTerm, TermType


class Query(graphene.ObjectType):
    term = graphene.Field(TermType, id=graphene.ID())
    terms = graphene.List(TermType)
    questions = graphene.List(QuestionsType)
    answers = graphene.List(AnswersType)

    def resolve_term(self, info, id):
        return Terms.objects.get(pk=id)

    def resolve_terms(self, info):
        return Terms.objects.all()

    def resolve_questions(self, info):
        return Questions.objects.all()

    def resolve_answers(self, info):
        return Answers.objects.all()

class MyMutations(graphene.ObjectType):
    create_term = CreateTerm.Field()

schema = graphene.Schema(query=Query, mutation=MyMutations)
