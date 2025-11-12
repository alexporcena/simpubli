from django.shortcuts import render
from .models import DadosEstado
import wikipediaapi
# Views

def sobre(request):
    return render(request, 'sobre.html')

def index(request):

    wiki_wiki = wikipediaapi.Wikipedia(user_agent='Simpubli (merlin@example.com)', language='pt')
    page_py = wiki_wiki.page('São Paulo (estado)')


    primeiro_dado = DadosEstado.objects.first()

    context = {}

    if primeiro_dado:
        registro_id = primeiro_dado.id
        registro_json = primeiro_dado.json

        # 3. Prepara o contexto para o template
        context = {
            'registro_id': registro_id,
            'registro_json': registro_json,
            'json_formatado': registro_json, # Pode ser útil para exibição no template,
            'pagina': page_py.summary[0:1200] + '...',
            'link': page_py.fullurl,
            'tt' : page_py.title,
        }
    else:
        # Caso não haja registros
        context = {
            'mensagem': 'Nenhum registro encontrado na tabela dados_estado.'
        }
    
    return render(request, 'index.html', context)