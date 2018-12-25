# -*- coding: utf-8 -*-
from busdata.models import *

def criarEmpresas():
    nomeEmpresasList = ['Redentor','Barra','Feital','Vera Cruz']
    empresasInativasList = ['Feital']
    for nome in nomeEmpresasList:
        if not Empresa.objects.filter(nome=nome).exists():
            novaEmpresa = Empresa(nome=nome)
            if nome in empresasInativasList:
                novaEmpresa.is_active = False
            novaEmpresa.save()
            print "[first_load @ criarEmpresas] Nova empresa criada: ",novaEmpresa

def criarConsorcios():
    dictConsorciosList = []
    dictConsorciosList.append({'nome': 'Intermunicipal'})
    dictConsorciosList.append({'nome': 'BRT', 'cor': '#0000ff'})
    dictConsorciosList.append({'nome': 'Santa Cruz', 'cor': '#e31919'})
    dictConsorciosList.append({'nome': 'Transcarioca', 'cor': '#0d6fa8'})
    dictConsorciosList.append({'nome': 'Internorte', 'cor': '#a2b719'})
    dictConsorciosList.append({'nome': 'Intersul', 'cor': '#fdc418'})
    for d in dictConsorciosList:
        if not Consorcio.objects.filter(nome=d['nome']).exists():
            novoObj = Consorcio(nome=d['nome'])
            if 'cor' in d:
                novoObj.cor = d['cor']
            novoObj.save()
            print "[first_load @ criarConsorcios] Novo consorcio criado: ",novoObj

def criarFabricantes():
    nomesList = ['Neobus','Caio','Marcopolo','Comil','Mascarello',]
    for nome in nomesList:
        if not Fabricante.objects.filter(nome=nome).exists():
            novoObj = Fabricante(nome=nome)
            novoObj.save()
            print "[first_load @ criarFabricantes] Nova fabricante criada: ", novoObj

def criarCarrocerias():
    dictCarroceriasList = []
    dictCarroceriasList.append({'nome': 'Mega', 'fabricante': 'Neobus'})
    dictCarroceriasList.append({'nome': 'Mega Plus', 'fabricante': 'Neobus'})
    dictCarroceriasList.append({'nome': 'Spectrum City', 'fabricante': 'Neobus'})
    dictCarroceriasList.append({'nome': 'Mega BRT', 'fabricante': 'Neobus'})
    dictCarroceriasList.append({'nome': 'Mega BRS', 'fabricante': 'Neobus'})
    dictCarroceriasList.append({'nome': 'Paradiso', 'fabricante': 'Marcopolo'})
    dictCarroceriasList.append({'nome': 'Torino', 'fabricante': 'Marcopolo'})
    dictCarroceriasList.append({'nome': 'Viaggio', 'fabricante': 'Marcopolo'})
    dictCarroceriasList.append({'nome': 'Viale', 'fabricante': 'Marcopolo'})
    dictCarroceriasList.append({'nome': 'Ideale', 'fabricante': 'Marcopolo'})
    dictCarroceriasList.append({'nome': 'Senior', 'fabricante': 'Marcopolo'})
    dictCarroceriasList.append({'nome': 'Apache Vip', 'fabricante': 'Caio'})
    dictCarroceriasList.append({'nome': 'Millennium', 'fabricante': 'Caio'})
    dictCarroceriasList.append({'nome': 'Mondego', 'fabricante': 'Caio'})
    dictCarroceriasList.append({'nome': 'Foz Super', 'fabricante': 'Caio'})
    dictCarroceriasList.append({'nome': 'Foz', 'fabricante': 'Caio'})
    dictCarroceriasList.append({'nome': 'Svelto', 'fabricante': 'Comil'})
    dictCarroceriasList.append({'nome': 'Campione', 'fabricante': 'Comil'})
    dictCarroceriasList.append({'nome': 'Svelto Midi', 'fabricante': 'Comil'})
    dictCarroceriasList.append({'nome': 'GranVia Midi', 'fabricante': 'Mascarello'})
    dictCarroceriasList.append({'nome': 'Roma', 'fabricante': 'Mascarello'})
    for d in dictCarroceriasList:
        if not Carroceria.objects.filter(nome=d['nome']).exists():
            novoObj = Carroceria(nome=d['nome'])
            fabricanteObj = Fabricante.objects.filter(nome=d['fabricante'])
            if fabricanteObj:
                novoObj.fabricante = fabricanteObj.first()
            else:
                print "- ! - [first_load @ criarCarrocerias] Erro: Carroceria não foi criada: ", d
                continue
            novoObj.save()
            print "[first_load @ criarCarrocerias] Nova carroceria criada: ",novoObj
