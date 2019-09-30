from django.db import models

# Create your models here.
class Propriedade(models.Model):

    idApi = models.IntegerField("ID da aplicação anterior")
    nome = models.CharField(verbose_name="Nome", max_length=40)
    nomeProprietario = models.CharField(verbose_name="Nome do Proprietário", max_length=40)
    qtdAtual = models.DecimalField(verbose_name="Quantidade atual de Kg na Propriedade", max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Propriedade'
        verbose_name_plural = 'Propriedades'
        ordering = ['nome']