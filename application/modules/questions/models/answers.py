from django.db import models


class Answers(models.Model):
    description = models.TextField(blank=False)
    right = models.BoolField(default=False)
    questions_id = models.ForeignKey('Question', blank=False, on_delete=models.CASCADE)