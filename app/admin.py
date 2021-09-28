from django.contrib import admin
from .models import Musicas

class ProdutoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'autor', 'link')

admin.site.register(Musicas, ProdutoAdmin)
