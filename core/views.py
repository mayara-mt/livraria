from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from core.models import Categoria

import json


@method_decorator(csrf_exempt, name='dispatch')
class CategoriaView(View):
    def get(self, request, id=None):
        if id:
            query_set = Categoria.objects.get(id)
            data = {'id': query_set.id, 'descricao': query_set.descricao}
            return JsonResponse(data)
        else:
            data = list(Categoria.objects.values())
            formatted_data = json.dumps(data, ensure_ascii=False)
            return HttpResponse(formatted_data, content_type='application/json')

    def post(self, request):
        json_data = json.loads(request.body)
        nova_categoria = Categoria.object.create(**json_data)
        data = {'id': nova_categoria.id, 'descricao': nova_categoria.descricao}
        return JsonResponse(data)

    def patch(self, request, id):
        json_data = json.loads(request.body)
        query_set = Categoria.objects.get(id=id)
        query_set.descricao = json_data['descricao'] if 'descricao' in json_data else query_set.descricao
        query_set.save()
        data = {'id': query_set.id, 'descricao': query_set.descricao}
        return JsonResponse(data)

    def delete(self, request, id):
        query_set = Categoria.objects.get(id=id)
        query_set.delete()
        data = {'mensagem': 'Item excluido com sucesso.'}
        return JsonResponse(data)