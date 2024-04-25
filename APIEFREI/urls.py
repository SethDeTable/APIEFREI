"""
URL configuration for APIEFREI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from APFLORIAN import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/items/<int:item_id>/', views.get_item_by_id, name='item_detail'),
    path('api/moves/<int:move_id>/', views.get_move_by_id, name='move_detail'),
    path('api/pokemon/<int:pokemon_id>/', views.get_pokemon_by_id, name='pokemon_detail'),
    path('api/pokemon/<str:pokemon_name>/', views.get_pokemon_by_name, name='pokemon_name_detail'),
    path('api/pokemon/types/<str:pokemon_identifier>/', views.get_pokemon_by_type, name='pokemon_type_detail'),
    path('api/connexion/', views.connexion, name='connexion'),
    path('api/register/', views.register, name='register'),
    path('api/mesPokemons/', views.mes_pokemons, name='mes_pokemons'),
    path('api/role/', views.role, name='role'),
    path('api/admin/users/', views.admin_users, name='admin_users'),
]
