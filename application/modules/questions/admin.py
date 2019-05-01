from django.contrib import admin

from .models import Answers, Questions, Terms


class AnswersAdmin(admin.ModelAdmin):
    list_display = ('questions_id', 'description', 'right')


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('terms_id', 'description')


class TermsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


admin.site.register(Answers, AnswersAdmin)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Terms, TermsAdmin)
