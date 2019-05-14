from django.db import models


class Answers(models.Model):
    description = models.TextField(blank=False)
    img_url = models.TextField(blank=True)
    right = models.BooleanField(default=False)
    questions = models.ForeignKey('Questions', blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
