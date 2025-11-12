from django.shortcuts import render
from .models import DadosEstado
from .models import DadosMunicipios
import wikipediaapi
import random

# Views

def sobre(request):
    return render(request, 'sobre.html')

def pesquisar(request):
    municipio_encontrado = None
    resultados_json = None
    
    todos_municipios = DadosMunicipios.objects.all().order_by('id_ibge')
    if request.method == 'GET':
        id_ibge_selecionado = request.GET.get('municipio')
        
        if id_ibge_selecionado:
            try:
                municipio_encontrado = DadosMunicipios.objects.get(id_ibge=id_ibge_selecionado)
                resultados_json = municipio_encontrado.json
            except DadosMunicipios.DoesNotExist:
                municipio_encontrado = None

    context = {
        'todos_municipios': todos_municipios,
        'municipio_encontrado': municipio_encontrado,
        'resultados_json': resultados_json,
    }
    
    return render(request, 'pesquisar.html', context)

def comparar(request):
    municipio_encontrado_1 = None
    resultados_json_1 = None

    municipio_encontrado_2 = None
    resultados_json_2 = None
    
    todos_municipios = DadosMunicipios.objects.all().order_by('id_ibge')

    if request.method == 'POST':
        id_ibge_selecionado_1 = request.POST.get('municipio1')
        id_ibge_selecionado_2 = request.POST.get('municipio2')
        
        if id_ibge_selecionado_1 and id_ibge_selecionado_2:
            try:
                municipio_encontrado_1 = DadosMunicipios.objects.get(id_ibge=id_ibge_selecionado_1)
                municipio_encontrado_2 = DadosMunicipios.objects.get(id_ibge=id_ibge_selecionado_2)
                resultados_json_1 = municipio_encontrado_1.json
                resultados_json_2 = municipio_encontrado_2.json
            except DadosMunicipios.DoesNotExist:
                municipio_encontrado = None

    context = {
        'todos_municipios': todos_municipios,
        'resultados_json_1': resultados_json_1,
        'resultados_json_2': resultados_json_2,
    }
    
    return render(request, 'comparar.html', context)

def aleatorio(request):
    municipio_encontrado = None
    resultados_json = None
    id_selecionado = random.randint(1, 644)



    if id_selecionado:
        try:
            municipio_encontrado = DadosMunicipios.objects.get(id=id_selecionado)
            resultados_json = municipio_encontrado.json
        except DadosMunicipios.DoesNotExist:
                municipio_encontrado = None
    context = {
        'municipio_encontrado': municipio_encontrado,
        'resultados_json': resultados_json,
    }
    
    return render(request, 'aleatorio.html', context)

def index(request):

    wiki_wiki = wikipediaapi.Wikipedia(user_agent='Simpubli (merlin@example.com)', language='pt')
    page_py = wiki_wiki.page('São Paulo (estado)')


    primeiro_dado = DadosEstado.objects.first()

    context = {}

    if primeiro_dado:
        registro_id = primeiro_dado.id
        registro_json = primeiro_dado.json

        context = {
            'registro_id': registro_id,
            'registro_json': registro_json,
            'json_formatado': registro_json,
            'pagina': page_py.summary[0:1200] + '...',
            'link': page_py.fullurl,
            'tt' : page_py.title,
        }
    else:
        context = {
            'mensagem': 'Nenhum registro encontrado na tabela dados_estado.'
        }
    
    return render(request, 'index.html', context)