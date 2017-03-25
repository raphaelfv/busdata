# -*- coding: utf-8 -*-
from django.db import models

# Foto* (upload via arquivo ou link) (path)
# Fonte* (desconhecida, própria ou link) (char)
# Ano* (int)
# Linha* (char)
# Empresa* (class)
# Consórcio* (class)
# Número de ordem (char)
# Local (char)

class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100,unique=True)
    # consorcio = models.ManyToManyField('Consorcio')

    # def natural_key(self):
    #     return (self.id, self.nome_levan)

    class Meta:
        managed = True
        db_table = 'empresa'

class Consorcio(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100,unique=True)
    cor = models.CharField(max_length=10,blank=True, null=True)

    # def natural_key(self):
    #     return (self.id, self.nome_levan)

    class Meta:
        managed = True
        db_table = 'consorcio'

class Registro(models.Model):
    id = models.AutoField(primary_key=True)
    foto = models.CharField(max_length=100)
    ano = models.IntegerField()
    linha = models.CharField(max_length=10)
    empresa = models.ForeignKey('Empresa')
    consorcio = models.ForeignKey('Consorcio')
    ordem = models.CharField(max_length=10,blank=True, null=True)
    local = models.CharField(max_length=200,blank=True, null=True)

    # def natural_key(self):
    #     return (self.id, self.nome_levan)

    class Meta:
        managed = True
        db_table = 'registro'
