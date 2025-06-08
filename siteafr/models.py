from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=80)
    idade = models.IntegerField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

