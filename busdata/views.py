from busdata.models import *
from busdata.form_models import *

from django.apps import apps
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

def inventario(request):

    empresas = Empresa.objects.all()
    registros = Registro.objects.all()
    consorcios = Consorcio.objects.all()

    return render(request, 'html/inventario.html',
                  {'registros': registros, 'empresas':empresas,'consorcios':consorcios}
                  )

def cadastrarFoto(request,registroID=None):

    if registroID:
        obj = get_object_or_404(Registro, id=registroID)
    else:
        obj = None

    formRegistro = RegistroForm(instance=obj)
    if request.method == 'POST':
        formRegistro = RegistroForm(request.POST,instance=obj)
        if formRegistro.is_valid():
            novoRegistro = formRegistro.save()
            messages.success(request,"Registro salvo com sucesso")
            return redirect('/cadastro/registro/' + str(novoRegistro.id))
        else:
            print '[views 33] Ocorreu um erro no cadastro',formRegistro.errors
        mensagem_erro = 'Ocorreu um erro no cadastro'
        messages.error(request,mensagem_erro)
    return render(request, 'html/cadastro.html',{'formRegistro': formRegistro,})
