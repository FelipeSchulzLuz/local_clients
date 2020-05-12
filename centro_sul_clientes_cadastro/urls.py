from django.urls import path
from . import views


urlpatterns = [
     path('', views.index, name="index"),
     path('cliente/<int:pk>/', views.detalhe_cliente, name="detalhe_cliente"),
     path('cliente/edit/<int:pk>/', views.editar_cliente, name="edit_cliente"),
     path('cliente/new/', views.adicionar_cliente, name="adicionar_cliente"),
     path('cliente/lista/', views.ClienteListView.as_view() , name="lista_clientes"),
     
]