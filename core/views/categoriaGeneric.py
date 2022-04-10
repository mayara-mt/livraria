from core.models import Categoria
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from core.serializers.categoriaSerializer import CategoriaSerializer


class CategoriasListGeneric(ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriaDetailGeneric(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
