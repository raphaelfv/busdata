# -*- coding: utf-8 -*-
from busdata.models import *
from django.forms import ModelForm
from django import forms
from django.utils.translation import ugettext_lazy as _

class RegistroForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Registro
        fields = '__all__'
        exclude = ['dataInclusao']

class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'
        labels = {
            'nome': _('Nome da empresa (simplificado)'),
        }
    def clean_nome(self): #validacao de erro: clean_nomeAtributo
        nome = self.cleaned_data['nome']
        if Empresa.objects.filter(nome=nome).exists:
            print 'A empresa %s já existe' % nome
            raise forms.ValidationError("Esta empresa já esta cadastrada")
        return nome
