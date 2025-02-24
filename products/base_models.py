from django.db import models


class BaseModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True