from django.db import models

# Criar dados para ligar ao banco de dados


class Pessoa(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
