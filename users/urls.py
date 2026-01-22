from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_producteur, name='register_producteur'),
    path('dashboard/', views.dashboard_producteur, name='dashboard_producteur'),
]
