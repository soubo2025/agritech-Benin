from django.urls import path
from .views import liste_recoltes

urlpatterns = [
    path('recoltes/', liste_recoltes, name='liste_recoltes'),
]




from django.urls import path
from .views import recolte_list

urlpatterns = [
    path('recoltes/', recolte_list, name='recolte_list'),
]
