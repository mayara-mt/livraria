from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from core.models import ItensCompra


class CriarEditarItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ('livro', 'quantidade')

    def validate(self, data):
        if data['quantidade'] > data['livro'].quantidade:
            raise serializers.ValidationError({
                'quantidade': 'Quantidade solicitada não disponivel em estoque.'
            })
        return data


class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()

    class Meta:
        model = ItensCompra
        fields = ('livro', 'quantidade', 'total')
        depth = 1

    def get_total(self, instance):
        return instance.quantidade * instance.livro.preco
