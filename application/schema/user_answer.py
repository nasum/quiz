import graphene
from graphene_django import DjangoObjectType
from modules.questions.models import UserAnswer


class UserAnswerType(DjangoObjectType):
    class Meta:
        model = UserAnswer
    answers_id = graphene.Int()
    user_id = graphene.String()


class CreateUserAnswer(graphene.Mutation):
    user_answer = graphene.Field(UserAnswerType)

    class Arguments:
        answers_id = graphene.Int(required=True)
        user_id = graphene.String(required=True)

    def mutate(self, info, answers_id, user_id):
        user_answer = UserAnswer.objects.create(answers_id=answers_id, user_id=user_id)

        return CreateUserAnswer(user_answer=user_answer)
