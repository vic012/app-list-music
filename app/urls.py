from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('musica/<int:pk>/', views.musica, name='musicas'),
]