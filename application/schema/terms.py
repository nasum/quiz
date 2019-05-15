import graphene
from graphene_django import DjangoObjectType
from modules.questions.models import Questions, Terms, Answers
from schema.questions import QuestionsType, QuestionsInputType
from schema.answers import AnswersType


class TermType(DjangoObjectType):
    class Meta:
        model = Terms

    id = graphene.ID()
    title = graphene.String()
    questions = graphene.List(QuestionsType)


class CreateTerm(graphene.Mutation):
    term = graphene.Field(TermType)
    question = graphene.Field(QuestionsType)
    answer = graphene.Field(AnswersType)

    class Arguments:
        title = graphene.String(required=True)
        questions = graphene.List(QuestionsInputType)

    def mutate(self, info, title, questions):
        term = Terms.objects.create(title=title)

        for question in questions:
            question_obj = Questions.objects.create(terms=term, description=question.description)
            for answer in question.answers:
                Answers.objects.create(
                    questions=question_obj,
                    description=answer.description,
                    img_url=answer.img_url,
                    right=answer.right
                )

        return CreateTerm(term=term)
