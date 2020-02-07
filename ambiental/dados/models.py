from django.db import models

class Dados(models.Model):
    zona = models.TextField()
    bairro = models.TextField()
    rua = models.TextField()
    nome = models.TextField()
    area_min = models.IntegerField()
    testada_min = models.IntegerField()
    taxa_ocp = models.TextField()
    taxa_prm = models.IntegerField()
    num_pav = models.IntegerField()
    coef_aprov = models.FloatField()
    agua = models.TextField()
    esgoto = models.TextField()
    lixo = models.TextField()

class TSeptico(models.Model):
    num_pessoas = models.IntegerField()
    C = models.IntegerField()
    contr_dia = models.IntegerField()
    T = models.FloatField()
    K = models.IntegerField()
    Lf = models.IntegerField()
    volume_util_L = models.FloatField()
    volume_util_M = models.FloatField()
    alt_adotada = models.FloatField()
    area = models.FloatField()
    diametro = models.FloatField()

class FiltroBAA(models.Model):
    num_pessoas = models.IntegerField()
    C = models.IntegerField()
    contr_dia = models.IntegerField()
    T = models.FloatField()
    volume_util_L = models.FloatField()
    volume_util_M = models.FloatField()
    area = models.FloatField()
    diametro = models.FloatField()

class Formulario(models.Model):
    bairro = models.TextField()
    nome = models.TextField()
    logradouro = models.TextField()
    area = models.FloatField()
    area_planta = models.FloatField()
    num_pav = models.IntegerField()
    num_pessoas = models.IntegerField()

class FormularioCondVertical(models.Model):
    num_lotes = models.IntegerField()
    num_predios = models.IntegerField()

class Tanque(models.Model):
    comprimento = models.FloatField()
    largura = models.FloatField()

class OpcaoForm(models.Model):
    possui_construcao = models.TextField()
    tela = models.TextField()
    wetlands = models.TextField()