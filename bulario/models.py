from django.db import models

class Search(models.Model):
    nomeMedicamento = models.CharField(max_length=255)
