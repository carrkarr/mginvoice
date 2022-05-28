from django.urls import path
from . import views

from fac.views import list_fac_view, update_fac_view

urlpatterns = [
    path('import-fac/',views.upload_fac, name ='import-fac'),
    path('act_load_fac/',views.act_load_fac, name ='act_load_fac'),
    path('create_fac/', views.create_fac, name='create_fac'),
    #path('list_fac/', views.list_fac, name='list_fac'),
    path('list_fac/', list_fac_view.as_view(), name='list-fac'),
    path('find_fac/', views.list_fac_view, name='find_fac'),
    path('del_fac/', views.update_fac, name='del_fac'),
    path('update-fac-view/<int:id>', update_fac_view.as_view(), name='update_fac_view'),
    #path('order-detail/<int:pk>/',OrderView.as_view(),name='order_view')

]
