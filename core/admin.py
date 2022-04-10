from django.contrib import admin

from core.models import Autor, Categoria, Compra, Editora, Livro, ItensCompra

admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Livro)


# Classe para facilitar a visualização dos itens da compra
class ItensInline(admin.TabularInline):
    model = ItensCompra


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = (ItensInline,)