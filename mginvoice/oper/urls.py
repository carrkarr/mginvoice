from django.urls import path
from . import views

#from fac.views import list_fac_view, update_fac_view, delete_fac

urlpatterns = [
    path('create_depo/', views.create_depo, name='create_depo'),
    path('list_depo/', views.list_depo_view, name='list-depo'), # Funcion
    path('find_depo/', views.find_depo, name='find_depo'),
    path('find_depo_f/', views.find_depo_f, name='find_depo_f'),
    path('del_depo/<int:id>/',views.delete_depo, name='del_depo'),
]
