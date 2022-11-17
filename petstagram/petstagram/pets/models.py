# pets/models.py

from django.db import models


class Pet(models.Model):
    MAX_NAME = 30

    name = models.CharField(
        max_length=MAX_NAME,
        null=False,
        blank=False,
    )

    personal_photo = models.URLField(
        
    )
