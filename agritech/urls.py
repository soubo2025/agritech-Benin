from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentification Django (login, logout, password reset...)
    path('accounts/', include('django.contrib.auth.urls')),

    # Applications
    path('production/', include('production.urls')),
    path('stockage/', include('stockage.urls')),
    path('users/', include('users.urls')),
    path('dashboard/', include('dashboard.urls')),

    # Page d'accueil
    path('', include('core.urls')),
]
