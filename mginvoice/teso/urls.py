from django.urls import path
from . import views

app_name = 'teso'

urlpatterns = [
    path('list_depo_up/', views.list_depo_up_view, name='list-depo-up'), # Funcion, Pantalla principal
    path('create_depo/', views.create_depo, name='create-depo'),
    path('update_depo/<int:pk>/edit', views.edit_depo, name='edit-depo'),
    path('find_depo_up/', views.find_depo_up, name='find_depo-up'),
    path('find_depo_f_up/', views.find_depo_f_up, name='find_depo_f-up'),

    path('list_fac_reparto/', views.list_fac_reparto_view, name='list-fac-reparto'), # Funcion, Pantalla principal
    path('create_reparto/', views.create_reparto, name='create-reparto'),
    path('find_fac_r/', views.find_fac, name='find-fac-r'),
    path('find_fac_r_f/', views.find_fac_f, name='find-fac-r-f'),

    #path('create_efe/', views.create_efe, name='create-efe'),
    #path('list_depo/', views.list_depo_view, name='list-depo'), # Funcion
    #path('find_depo/', views.find_depo, name='find_depo'),
    #path('find_depo_f/', views.find_depo_f, name='find_depo_f'),


]
