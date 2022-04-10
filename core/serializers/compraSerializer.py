from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
from rest_framework import serializers
from core.models import Compra, ItensCompra
from core.serializers.itensCompraSerializer import ItensCompraSerializer, CriarEditarItensCompraSerializer


class CompraSerializer(ModelSerializer):
    usuario = CharField(source='usuario.email')
    status = SerializerMethodField()
    itens = ItensCompraSerializer(many=True)

    class Meta:
        model = Compra
        fields = ('id', 'status', 'usuario', 'itens', 'total')

    def get_status(self, instance):
        return instance.get_status_display()


class CriarEditarCompraSerializer(ModelSerializer):
    itens = CriarEditarItensCompraSerializer(many=True)
    usuario = serializers.HiddenField(default=serializers.CurrentUserDefault()) # Se não informado, será usado o usuario da request

    class Meta:
        model = Compra
        fields = ('usuario', 'itens')

    def create(self, validated_data):
        itens = validated_data.pop('itens')
        compra = Compra.objects.create(**validated_data)
        for item in itens:
            ItensCompra.objects.create(compra=compra, **item)
        compra.save()
        return compra

    def update(self, instance, validated_data):
        itens = validated_data.pop('itens')
        if itens:
            instance.itens.all().delete()
            for item in itens:
                ItensCompra.objects.create(compra=instance, **item)
            instance.save()
        return instance
