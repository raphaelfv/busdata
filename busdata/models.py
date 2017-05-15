# -*- coding: utf-8 -*-
from django.db import models

from django import forms
from django.forms import ModelForm, CharField, TextInput

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

    def __str__(self):
      return self.nome.encode('utf-8')

    class Meta:
        managed = True
        db_table = 'empresa'

class Consorcio(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100,unique=True)
    cor = models.CharField(max_length=10,blank=True, null=True)

    def __str__(self):
      return self.nome.encode('utf-8')

    class Meta:
        managed = True
        db_table = 'consorcio'

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100,unique=True)
    url = models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
      return self.nome.encode('utf-8')+' <'+self.url+'>'

    class Meta:
        managed = True
        db_table = 'autor'

class Registro(models.Model):
    id = models.AutoField(primary_key=True)
    foto = models.CharField(max_length=100)
    ano = models.IntegerField()
    linha = models.CharField(max_length=10)
    empresa = models.ForeignKey('Empresa')
    consorcio = models.ForeignKey('Consorcio')
    ordem = models.CharField(max_length=10,blank=True, null=True)
    local = models.CharField(max_length=200,blank=True, null=True)
    autor = models.ForeignKey('Autor',blank=True, null=True, default=None)
    fonte = models.CharField(max_length=200,blank=True)
    dataInclusao = models.DateField( auto_now_add=True)

    def __str__(self):
      return self.foto.encode('utf-8')

    class Meta:
        managed = True
        db_table = 'registro'
