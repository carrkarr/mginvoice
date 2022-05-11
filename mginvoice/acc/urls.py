from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name ="home"),
    path('menu/', views.menu_user, name ='menu'),
    path('logout/', views.logout_user, name='logout'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='acc/password_reset.html'), name='password_reset'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="acc/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='acc/password_reset_complete.html'), name='password_reset_complete'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name= 'acc/password_reset_done.html'), name='password_reset_done'),

    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),

]
