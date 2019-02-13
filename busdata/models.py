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

class Fabricante(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100,unique=True)

    def __str__(self):
      return self.nome.encode('utf-8')

    class Meta:
        managed = True
        db_table = 'fabricante'

class Carroceria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100,unique=True)
    fabricante = models.ForeignKey('Fabricante')

    def __str__(self):
      return self.fabricante.nome.encode('utf-8') + " " + self.nome.encode('utf-8')

    class Meta:
        managed = True
        db_table = 'carroceria'


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100,unique=True)
    url = models.CharField(max_length=100,blank=True, null=True) # URL do site

    def __str__(self):
        if self.url:
            return self.nome.encode('utf-8')+' <'+self.url+'>'
        return self.nome.encode('utf-8')


    class Meta:
        managed = True
        db_table = 'autor'

class Registro(models.Model):
    id = models.AutoField(primary_key=True)
    foto = models.CharField(max_length=100)
    ano = models.IntegerField()
    linha = models.CharField(max_length=10)
    empresa = models.ForeignKey('Empresa')
    consorcio = models.ForeignKey('Consorcio',blank=True, null=True)
    ordem = models.CharField(max_length=10,blank=True, null=True)
    local = models.CharField(max_length=200,blank=True, null=True)
    autor = models.ForeignKey('Autor', blank=True, null=True, default=None)
    carroceria = models.ForeignKey('Carroceria', blank=True, null=True, default=None)
    fonte = models.CharField(max_length=200,blank=True) # URL da fonte
    dataInclusao = models.DateField( auto_now_add=True)
    #TODO - last modified
    #TODO - user que criou o registro != autor

    def __str__(self):
      return self.foto.encode('utf-8')

    class Meta:
        managed = True
        db_table = 'registro'
