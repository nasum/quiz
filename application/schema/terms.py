import graphene
from graphene_django import DjangoObjectType
from modules.questions.models import Questions, Terms
from schema.questions import QuestionsType


class TermType(DjangoObjectType):
    class Meta:
        model = Terms
    
    title = graphene.String()
    questions = graphene.List(QuestionsType)

class CreateTerm(graphene.Mutation):
    term = graphene.Field(TermType)

    class Arguments:
        title = graphene.String(required=True)
        questions = graphene.List(graphene.String)
    
    def mutate(self, info, title, questions):
        term = Terms.objects.create(title=title)

        for question in questions:
            Questions.objects.create(terms=term, description=question)

        return CreateTerm(term)
