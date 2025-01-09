
from django.db import models

class Lista(models.Model):
    cod_produto = models.IntegerField()
    des_produto = models.CharField(max_length=255)  # Usando CharField para texto curto
    qtd_produtos = models.IntegerField()
    validade_produto = models.DateField()
    setor = models.CharField(max_length=255)  # Usando CharField para texto curto

    def __str__(self):
        return f"{self.cod_produto} - {self.des_produto}"
