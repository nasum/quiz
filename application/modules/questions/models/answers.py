from django.db import models


class Answers(models.Model):
    description = models.TextField(blank=False)
    right = models.BooleanField(default=False)
    questions = models.ForeignKey('Questions', blank=False, on_delete=models.CASCADE)