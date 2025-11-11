from django.shortcuts import render
from .models import DadosEstado
# Views

def sobre(request):
    return render(request, 'sobre.html')

def index(request):
    primeiro_dado = DadosEstado.objects.first()

    context = {}

    if primeiro_dado:
        registro_id = primeiro_dado.id
        registro_json = primeiro_dado.json

        # 3. Prepara o contexto para o template
        context = {
            'registro_id': registro_id,
            'registro_json': registro_json,
            'json_formatado': registro_json, # Pode ser útil para exibição no template
        }
    else:
        # Caso não haja registros
        context = {
            'mensagem': 'Nenhum registro encontrado na tabela dados_estado.'
        }
    
    return render(request, 'index.html', context)