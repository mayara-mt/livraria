from django.db import models

from core.models.compra import Compra
from core.models.livro import Livro


class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='itens')
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT, related_name='+') # Simbolo + significa que nao irá gerar o reverso
    quantidade = models.IntegerField()


