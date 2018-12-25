# -*- coding: utf-8 -*-
# Adiciona modelos ao /admin/
from django.contrib import admin
from .models import Empresa, Autor, Registro, Carroceria, Fabricante, Consorcio

admin.site.register(Consorcio)
admin.site.register(Fabricante)
admin.site.register(Carroceria)
admin.site.register(Empresa)
admin.site.register(Autor)
admin.site.register(Registro)

# Carrega dados atraves de funcoes do first_load
from busdata.first_load import criarCarrocerias,criarConsorcios,criarEmpresas,criarFabricantes
from busdata.settings import DEBUG

if DEBUG:
    criarEmpresas()
    criarConsorcios()
    criarFabricantes()
    criarCarrocerias()
