from django.db import models


class Questions(models.Model):
    description = models.TextField(blank=False)
    terms = models.ForeignKey('Terms', blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
