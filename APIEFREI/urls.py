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
    path('api/items/<int:id>/', views.items_list, name='item_detail'),
    path('api/moves/<int:move_id>/', views.moves_list, name='move_detail'),
    path('api/pokemon/<int:pokemon_id>/', views.pokemon_list, name='pokemon_detail'),
    #path('api/pokemon/<str:pokemon_name>/', views.pokemon_detail, name='pokemon_name_detail'),
    path('api/pokemon/types/<str:pokemon_identifier>/', views.types_list, name='pokemon_type_detail'),
    #--------------------------------------------------------
    path('items/<int:id>/', views.item_detail, name='item_detail'),
    path('moves/<int:id>/', views.move_detail, name='move_detail'),
    path('pokemon/<int:id>/', views.pokemon_detail, name='pokemon_detail'),
    path('egggroups/<int:id>/', views.egg_group_detail, name='egg_group_detail'),
    path('locations/<int:id>/', views.location_detail, name='location_detail'),
    path('pokemon_egggroups/<int:id>/', views.pokemon_egg_group_detail, name='pokemon_egg_group_detail'),
    path('pokemon_form_generations/<int:id>/', views.pokemon_form_generation_detail, name='pokemon_form_generation_detail'),
    path('pokemon_moves/<int:id>/', views.pokemon_move_detail, name='pokemon_move_detail'),
    path('pokemon_stats/<int:id>/', views.pokemon_stat_detail, name='pokemon_stat_detail'),
    path('pokemon_types/<int:id>/', views.pokemon_type_detail, name='pokemon_type_detail'),
    path('stats/<int:id>/', views.stat_detail, name='stat_detail'),
    path('types/<int:id>/', views.type_detail, name='type_detail'),
    #path('api/connexion/', views.connexion, name='connexion'),
    #path('api/register/', views.register, name='register'),
    #path('api/mesPokemons/', views.mes_pokemons, name='mes_pokemons'),
    #path('api/role/', views.role, name='role'),
    #path('api/admin/users/', views.admin_users, name='admin_users'),
]
