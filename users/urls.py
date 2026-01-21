



from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register_producteur, name='register_producteur'),
    path('dashboard/', views.dashboard_producteur, name='dashboard_producteur'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
]


