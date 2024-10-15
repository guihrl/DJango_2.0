from django.db import models

class Dono(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    balcao = models.ForeignKey(
        "Balcao", on_delete=models.CASCADE)
    frutas = models.ForeignKey(
        "Fruta", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
class Balcao(models.Model):
    nome_balcao= models.CharField(max_length=50)
    def __str__(self):
        return self.nome_balcao

class Fruta(models.Model):
    nome_fruta = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_fruta
