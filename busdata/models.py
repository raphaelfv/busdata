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
    is_active = models.BooleanField(default=True)

    def __str__(self):
      return self.nome

    class Meta:
        managed = True
        db_table = 'empresa'

class Consorcio(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100,unique=True)
    cor = models.CharField(max_length=10,blank=True, null=True)

    def __str__(self):
      return self.nome

    class Meta:
        managed = True
        db_table = 'consorcio'

class Fabricante(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100,unique=True)

    def __str__(self):
      return self.nome

    class Meta:
        managed = True
        db_table = 'fabricante'

class Carroceria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100,unique=True)
    fabricante = models.ForeignKey('Fabricante',on_delete=models.CASCADE,)

    def __str__(self):
      return self.fabricante.nome + " " + self.nome

    class Meta:
        managed = True
        db_table = 'carroceria'


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100,unique=True)
    url = models.CharField(max_length=100,blank=True, null=True) # URL do site

    def __str__(self):
        if self.url:
            return self.nome+' <'+self.url+'>'
        return self.nome

    class Meta:
        managed = True
        db_table = 'autor'

class Registro(models.Model):
    id = models.AutoField(primary_key=True)
    foto = models.CharField(max_length=100)
    ano = models.IntegerField()
    linha = models.CharField(max_length=10)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE,)
    consorcio = models.ForeignKey('Consorcio',blank=True, null=True, on_delete=models.CASCADE, verbose_name='Consórcio')
    ordem = models.CharField(max_length=10,blank=True, null=True)
    local = models.CharField(max_length=200,blank=True, null=True)
    autor = models.ForeignKey('Autor', blank=True, null=True, default=None, on_delete=models.CASCADE,)
    carroceria = models.ForeignKey('Carroceria', blank=True, null=True, default=None, on_delete=models.CASCADE,)
    fonte = models.CharField(max_length=200,blank=True) # URL da fonte
    dataInclusao = models.DateField( auto_now_add=True, verbose_name='Data de Inclusão')
    #TODO - last modified
    #TODO - user que criou o registro != autor

    def __str__(self):
        try:
            return self.foto
        except:
            return self.id

    class Meta:
        managed = True
        db_table = 'registro'
