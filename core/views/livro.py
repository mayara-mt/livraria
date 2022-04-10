from rest_framework.viewsets import ModelViewSet

from core.models import Livro
from core.serializers.livroSerializer import LivroSerializer, LivroDetailSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    # serializer_class = LivroSerializer

    def get_serializer_class(self):
        if 'list' == self.action:
            return LivroDetailSerializer
        if  'retrieve' == self.action:
            return LivroDetailSerializer
        return LivroSerializer
