from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
from core.models import Livro
from core.serializers.editoraSerializer import EditoraNestedSerializer


class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"


class LivroDetailSerializer(ModelSerializer):
    categoria = CharField(source='categoria.descricao') # Apresenta apenas a descrição na listagem
    editora = EditoraNestedSerializer()
    autores = SerializerMethodField()

    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1 # Desce 1 nivel no detalhamento de campos relacionados

    def get_autores(self, instance):
        nomes_autores = []
        autores = instance.autores.get_queryset()
        for autor in autores:
            nomes_autores.append(autor.nome)
        return nomes_autores