from django.db import models


class Terms(models.Model):
    title = models.CharField(max_length=256)
