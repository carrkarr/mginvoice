from django.urls import path
from . import views

urlpatterns = [
    path('list_depo_up/', views.list_depo_up_view, name='list-depo-up'), # Funcion, Pantalla principal
    
    path('create_depo/', views.create_depo, name='create-depo'),
    #path('movies/<int:pk>/edit', views.edit_movie, name='edit_movie'),
]
