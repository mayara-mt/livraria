from django.db import models


class Autor(models.Model):
    class Meta:
        verbose_name_plural = 'autores'
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

