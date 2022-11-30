from django.db import models

class Cadastro(models.Model):
    nome = models.CharField(max_length=30)
    usuario = models.CharField(max_length=30)
    senha = models.CharField(max_length=30)
    confirmarsenha = models.CharField(max_length=30)

