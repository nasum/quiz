import graphene

from modules.questions.models import Answers, Questions, Terms, UserAnswer
from schema.answers import AnswersType
from schema.questions import QuestionsType
from schema.terms import CreateTerm, TermType
from schema.user_answer import CreateUserAnswer, UserAnswerType


class Query(graphene.ObjectType):
    term = graphene.Field(TermType, id=graphene.ID())
    terms = graphene.List(TermType)
    questions = graphene.List(QuestionsType)
    answers = graphene.List(AnswersType)
    user_answers = graphene.List(UserAnswerType)

    def resolve_term(self, info, id):
        return Terms.objects.get(pk=id)

    def resolve_terms(self, info):
        return Terms.objects.all()

    def resolve_questions(self, info):
        return Questions.objects.all()

    def resolve_answers(self, info):
        return Answers.objects.all()

    def resolve_user_answer(self, info):
        return UserAnswer.objects.all()


class MyMutations(graphene.ObjectType):
    create_term = CreateTerm.Field()
    create_user_answer = CreateUserAnswer.Field()


schema = graphene.Schema(query=Query, mutation=MyMutations)
