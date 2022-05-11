from django.urls import path
from . import views

urlpatterns = [
    path('import-fac/',views.upload_fac, name ='import-fac'),
    path('act_load_fac/',views.act_load_fac, name ='act_load_fac'),
]
