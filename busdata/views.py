from django.shortcuts import render
from busdata.models import *
from busdata.form_models import *

from django.apps import apps

def inventario(request):

    empresas = Empresa.objects.all()
    registros = Registro.objects.all()
    consorcios = Consorcio.objects.all()
    print '-------------------'

    return render(request, 'html/inventario.html', {'registros': registros, 'empresas':empresas,'consorcios':consorcios})

def cadastrarEmpresa(request,empresaID=None):
    mensagem_erro = ''

    if empresaID:
        empresa = get_object_or_404(Poco, id=amostraID)
    else:
        empresa = None

    formEmpresa = EmpresaForm(instance=empresa)
    if request.method == 'POST':
        if formEmpresa.is_valid():
            novaEmpresa = formEmpresa.save()
            return render(request, 'html/cadastro.html', {'mensagem_sucesso': 'Empresa cadastrada com sucesso'})
        mensagem_erro = 'Ocorreu um erro no cadastro'
    return render(request, 'html/cadastro.html', {'mensagem_erro': mensagem_erro,
                                                    'form': formEmpresa,
                                                  })
