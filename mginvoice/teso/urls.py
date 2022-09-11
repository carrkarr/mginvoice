from django.urls import path
from . import views

urlpatterns = [
    path('list_depo_up/', views.list_depo_up_view, name='list-depo-up'), # Funcion, Pantalla principal
    path('create_depo/', views.create_depo, name='create-depo'),
    path('update_depo/<int:pk>/edit', views.edit_depo, name='edit-depo'),
    path('find_depo_up/', views.find_depo_up, name='find_depo-up'),
    path('find_depo_f_up/', views.find_depo_f_up, name='find_depo_f-up'),
]
