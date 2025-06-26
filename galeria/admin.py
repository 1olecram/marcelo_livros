from django.contrib import admin
from galeria.models import Livro


class ListandoLivros(admin.ModelAdmin):
    list_display = ("id", "titulo", "legenda","publicado")
    list_display_links = ("id", "titulo")
    search_fields = ("titulo",)
    list_filter = ("categoria",)
    list_editable = ("publicado",)
    list_per_page = 10
admin.site.register(Livro, ListandoLivros)

