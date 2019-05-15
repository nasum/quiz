from django.contrib import admin

from .models import Answers, Questions, Terms, UserAnswer


class AnswersAdmin(admin.ModelAdmin):
    list_display = ('questions_id', 'description', 'right', 'img_url')


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('terms_id', 'description')


class TermsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('answers', 'user_id')


admin.site.register(Answers, AnswersAdmin)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Terms, TermsAdmin)
admin.site.register(UserAnswer, UserAnswerAdmin)