from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('popup/', views.popup, name='popup'),
    path('serviceFinally/', views.service_finally, name='service_finally'),
    path('register/', views.register, name='register'),
    path('privacy-policy/', views.privacy_policy_view, name='privacy_policy'),
]
