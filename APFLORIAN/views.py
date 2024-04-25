from django.shortcuts import render
from .models import Items, Moves, Pokemon, EggGroups, Locations, PokemonEggGroups, PokemonFormGenerations, PokemonMoves, PokemonStats, PokemonTypes, Stats, Types
from django.views.decorators.http import require_http_methods,require_GET
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
import json
# Create your views here.


@require_GET
def items_list(request):
    items = Items.objects.all()
    items_list = [model_to_dict(item) for item in items]
    return JsonResponse(items_list, safe=False)

@require_GET
def moves_list(request):
    moves = Moves.objects.all()
    moves_list = [model_to_dict(move) for move in moves]
    return JsonResponse(moves_list, safe=False)

@require_GET
def pokemon_list(request):
    pokemon = Pokemon.objects.all()
    pokemon_list = [model_to_dict(p) for p in pokemon]
    return JsonResponse(pokemon_list, safe=False)

@require_GET
def egg_groups_list(request):
    egg_groups = EggGroups.objects.all()
    egg_groups_list = [model_to_dict(egg) for egg in egg_groups]
    return JsonResponse(egg_groups_list, safe=False)

@require_GET
def locations_list(request):
    locations = Locations.objects.all()
    locations_list = [model_to_dict(loc) for loc in locations]
    return JsonResponse(locations_list, safe=False)

@require_GET
def pokemon_egg_groups_list(request):
    pokemon_egg_groups = PokemonEggGroups.objects.all()
    pokemon_egg_groups_list = [model_to_dict(peg) for peg in pokemon_egg_groups]
    return JsonResponse(pokemon_egg_groups_list, safe=False)

@require_GET
def pokemon_form_generations_list(request):
    pokemon_form_generations = PokemonFormGenerations.objects.all()
    pokemon_form_generations_list = [model_to_dict(pfg) for pfg in pokemon_form_generations]
    return JsonResponse(pokemon_form_generations_list, safe=False)

@require_GET
def pokemon_moves_list(request):
    pokemon_moves = PokemonMoves.objects.all()
    pokemon_moves_list = [model_to_dict(pm) for pm in pokemon_moves]
    return JsonResponse(pokemon_moves_list, safe=False)

@require_GET
def pokemon_stats_list(request):
    pokemon_stats = PokemonStats.objects.all()
    pokemon_stats_list = [model_to_dict(ps) for ps in pokemon_stats]
    return JsonResponse(pokemon_stats_list, safe=False)

@require_GET
def pokemon_types_list(request):
    pokemon_types = PokemonTypes.objects.all()
    pokemon_types_list = [model_to_dict(pt) for pt in pokemon_types]
    return JsonResponse(pokemon_types_list, safe=False)

@require_GET
def stats_list(request):
    stats = Stats.objects.all()
    stats_list = [model_to_dict(stat) for stat in stats]
    return JsonResponse(stats_list, safe=False)

@require_GET
def types_list(request):
    types = Types.objects.all()
    types_list = [model_to_dict(typ) for typ in types]
    return JsonResponse(types_list, safe=False)

#------------------CRUD-------------------------------------------------------------
    
@require_http_methods(["GET", "DELETE", "PUT"])
def item_detail(request, id):
    item = get_object_or_404(Items, pk=id)
    if request.method == 'GET':
        return JsonResponse(model_to_dict(item))
    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status=204)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        for field, value in data.items():
            setattr(item, field, value)
        item.save()
        return JsonResponse(model_to_dict(item))

# Vue détaillée pour la table Moves
@require_http_methods(["GET", "DELETE", "PUT"])
def move_detail(request, id):
    move = get_object_or_404(Moves, pk=id)
    if request.method == 'GET':
        return JsonResponse(model_to_dict(move))
    elif request.method == 'DELETE':
        move.delete()
        return HttpResponse(status=204)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        for field, value in data.items():
            setattr(move, field, value)
        move.save()
        return JsonResponse(model_to_dict(move))

# Vue détaillée pour la table Pokemon
@require_http_methods(["GET", "DELETE", "PUT"])
def pokemon_detail(request, id):
    pokemon = get_object_or_404(Pokemon, pk=id)
    if request.method == 'GET':
        return JsonResponse(model_to_dict(pokemon))
    elif request.method == 'DELETE':
        pokemon.delete()
        return HttpResponse(status=204)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        for field, value in data.items():
            setattr(pokemon, field, value)
        pokemon.save()
        return JsonResponse(model_to_dict(pokemon))

# Vue détaillée pour la table EggGroups
@require_http_methods(["GET", "DELETE", "PUT"])
def egg_group_detail(request, id):
    egg_group = get_object_or_404(EggGroups, pk=id)
    if request.method == 'GET':
        return JsonResponse(model_to_dict(egg_group))
    elif request.method == 'DELETE':
        egg_group.delete()
        return HttpResponse(status=204)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        for field, value in data.items():
            setattr(egg_group, field, value)
        egg_group.save()
        return JsonResponse(model_to_dict(egg_group))

# Vue détaillée pour la table Locations
@require_http_methods(["GET", "DELETE", "PUT"])
def location_detail(request, id):
    location = get_object_or_404(Locations, pk=id)
    if request.method == 'GET':
        return JsonResponse(model_to_dict(location))
    elif request.method == 'DELETE':
        location.delete()
        return HttpResponse(status=204)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        for field, value in data.items():
            setattr(location, field, value)
        location.save()
        return JsonResponse(model_to_dict(location))
    
def pokemon_egg_group_detail(request, id):
    pokemon_egg_group = get_object_or_404(PokemonEggGroups, pk=id)
    if request.method == 'GET':
        return JsonResponse(model_to_dict(pokemon_egg_group))
    elif request.method == 'DELETE':
        pokemon_egg_group.delete()
        return HttpResponse(status=204)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        for field, value in data.items():
            setattr(pokemon_egg_group, field, value)
        pokemon_egg_group.save()
        return JsonResponse(model_to_dict(pokemon_egg_group))

# Vue détaillée pour la table PokemonFormGenerations
@require_http_methods(["GET", "DELETE", "PUT"])
def pokemon_form_generation_detail(request, id):
    pokemon_form_generation = get_object_or_404(PokemonFormGenerations, pk=id)
    if request.method == 'GET':
        return JsonResponse(model_to_dict(pokemon_form_generation))
    elif request.method == 'DELETE':
        pokemon_form_generation.delete()
        return HttpResponse(status=204)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        for field, value in data.items():
            setattr(pokemon_form_generation, field, value)
        pokemon_form_generation.save()
        return JsonResponse(model_to_dict(pokemon_form_generation))

# Vue détaillée pour la table PokemonMoves
@require_http_methods(["GET", "DELETE", "PUT"])
def pokemon_move_detail(request, id):
    pokemon_move = get_object_or_404(PokemonMoves, pk=id)
    if request.method == 'GET':
        return JsonResponse(model_to_dict(pokemon_move))
    elif request.method == 'DELETE':
        pokemon_move.delete()
        return HttpResponse(status=204)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        for field, value in data.items():
            setattr(pokemon_move, field, value)
        pokemon_move.save()
        return JsonResponse(model_to_dict(pokemon_move))

# Vue détaillée pour la table PokemonStats
@require_http_methods(["GET", "DELETE", "PUT"])
def pokemon_stat_detail(request, id):
    pokemon_stat = get_object_or_404(PokemonStats, pk=id)
    if request.method == 'GET':
        return JsonResponse(model_to_dict(pokemon_stat))
    elif request.method == 'DELETE':
        pokemon_stat.delete()
        return HttpResponse(status=204)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        for field, value in data.items():
            setattr(pokemon_stat, field, value)
        pokemon_stat.save()
        return JsonResponse(model_to_dict(pokemon_stat))

# Vue détaillée pour la table PokemonTypes
@require_http_methods(["GET", "DELETE", "PUT"])
def pokemon_type_detail(request, id):
    pokemon_type = get_object_or_404(PokemonTypes, pk=id)
    if request.method == 'GET':
        return JsonResponse(model_to_dict(pokemon_type))
    elif request.method == 'DELETE':
        pokemon_type.delete()
        return HttpResponse(status=204)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        for field, value in data.items():
            setattr(pokemon_type, field, value)
        pokemon_type.save()
        return JsonResponse(model_to_dict(pokemon_type))

# Vue détaillée pour la table Stats
@require_http_methods(["GET", "DELETE", "PUT"])
def stat_detail(request, id):
    stat = get_object_or_404(Stats, pk=id)
    if request.method == 'GET':
        return JsonResponse(model_to_dict(stat))
    elif request.method == 'DELETE':
        stat.delete()
        return HttpResponse(status=204)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        for field, value in data.items():
            setattr(stat, field, value)
        stat.save()
        return JsonResponse(model_to_dict(stat))

# Vue détaillée pour la table Types
@require_http_methods(["GET", "DELETE", "PUT"])
def type_detail(request, id):
    typ = get_object_or_404(Types, pk=id)
    if request.method == 'GET':
        return JsonResponse(model_to_dict(typ))
    elif request.method == 'DELETE':
        typ.delete()
        return HttpResponse(status=204)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        for field, value in data.items():
            setattr(typ, field, value)
        typ.save()
        return JsonResponse(model_to_dict(typ))