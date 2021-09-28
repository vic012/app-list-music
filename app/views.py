from django.shortcuts import render, get_object_or_404
from .models import Musicas

def index(request):
	musicas = Musicas.objects.all()
	context = {
		'musicas': musicas
	}
	return render(request, 'index.html', context)

def musica(request, pk):
	musica = get_object_or_404(Musicas, id=pk)
	context = {
		'musica': musica
	}
	return render(request, 'produto.html', context)