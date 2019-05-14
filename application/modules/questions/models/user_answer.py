from django.db import models


class UserAnswer(models.Model):
    answers = models.ForeignKey('Answers', blank=False, on_delete=models.CASCADE)
    user_id = models.TextField(blank=False)

    def __str__(self):
        return self.user_id
