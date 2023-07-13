from django.urls import path
from . import views

urlpatterns =[
    path('re/',views.regviews, name='register_url'),
    path('log/',views.loginviews, name='login_url'),
    path('lou/',views.logoutviews, name='logout_url'),
    path('sh/', views.Registrview, name='shop_url'),


]