# -*- coding: utf-8 -*-
from litoteca.models import *
from django.forms import ModelForm
from django import forms

class RegistroForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Registro
        fields = '__all__'
        exclude = ['dataInclusao']
