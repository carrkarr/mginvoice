from django.urls import path
from . import views
from django.conf.urls import handler400, handler403, handler404, handler500
#from acc.views import error_404

urlpatterns = [
    path('', views.home, name ="home"),
    path('login/', views.login_user, name ='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
]


#handler404 = error_404

#handler400 = error_400
#handler403 = error_403

#handler404 = error_404
# handler500 = error_500

