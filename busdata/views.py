from django.shortcuts import render

def cadastro(request):
#
#     mensagem = {}
#     active_tab = ''
#     midiasDict = {}
#     midiasDictJavascript = {}
#     dictTiposMidia = {}
#
#     # Se a URL tem ID da amostra, pega dados
#     if amostraID:
#         lamina = get_object_or_404(Lamina, id=amostraID)
#         midiasDict, midiasDictJavascript, dictTiposMidia = buscaMidias(lamina)
#     else:
#         lamina = None
#
#     # Cria formulario de lamina
#     formLamina = LaminaForm(instance=lamina)
#
#     # Cria formulario de midias
#     formMedia = MediaForm()
#
#     # Cria formulario de descricao microscopica
#     laminaDescricao = LaminaDescricao.objects.filter(lamina=amostraID)
#     if laminaDescricao:
#         formDescricaoLamina = LaminaDescricaoForm(instance=laminaDescricao[0])
#     else:
#         formDescricaoLamina = LaminaDescricaoForm(initial={'lamina': lamina})
#
#     # Se houve POST, pega nome e dados do formulario
#     if request.method == 'POST':
#         post = request.POST
#     else:
#         post = None
#
#     # Se houve POST, executa de acordo com o formulario enviado / botao apertado
#     if post:
#
#         # Forms da Lamina
#         if 'excluirAmostra' in post:
#             laminaExcluida = Lamina.objects.get(id=amostraID)
#             mensagem = excluirAmostra(laminaExcluida)
#             return redirect('/cadastro/lamina/2')
#
#         elif 'formLamina' in post:
#             # identificacao
#             formLamina = LaminaForm(post, instance=lamina)
#             if formLamina.is_valid():
#                 setSqlCursor('lamina')
#                 newLamina = formLamina.save(commit=False)
#                 newLamina.save()
#                 return redirect('/cadastro/lamina/1')
#
#         elif 'formDescricaoLamina' in post:
#             print laminaDescricao, type(laminaDescricao)
#             # Cria formulario de descricao microscopica
#             laminaDescricao = LaminaDescricao.objects.filter(lamina=amostraID)
#             if laminaDescricao:
#                 formDescricaoLamina = LaminaDescricaoForm(post, instance=laminaDescricao[0])
#             else:
#                 formDescricaoLamina = LaminaDescricaoForm(post)
# #            formDescricaoLamina = LaminaDescricaoForm(post, instance=laminaDescricao[0])
# #            print 'formDescricaoLamina', formDescricaoLamina
#             if formDescricaoLamina.is_valid():
#                 newLaminaDescricao = formDescricaoLamina.save(commit=False)
#                 print 'newLaminaDescricao', type(newLaminaDescricao)
#                 newLaminaDescricao.lamina = lamina #forca um dos atributos do formulario
#                 print 'lamina', lamina
#                 newLaminaDescricao.save()
#                 return redirect('/cadastro/lamina/1')
#
#         # Forms de Midia
#         elif 'baixarMidia' in post:
#             response = baixarMidia(post['baixarMidia'])
#             if isinstance(response, HttpResponse):
#                 return response
#             else:
#                 mensagem['erro'] = response
#         else:
#             mensagem, midiasDict, midiasDictJavascript, dictTiposMidia = validaFormMidia(lamina,request)
#             active_tab = 'midia'

#    formLamina = LaminaForm(instance=lamina)

    return render(request, 'html/cadastro.html', {})
