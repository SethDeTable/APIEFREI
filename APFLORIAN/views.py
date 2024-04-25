from django.shortcuts import render
from .models import Item
from django.views.decorators.http import require_http_methods,require_GET
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict

# Create your views here.

@require_GET
def item_list(request):     
    # Fetch all items     
    items = Item.objects.all()     
    items_list = [model_to_dict(item) for item in items]     
    return JsonResponse(items_list, safe=False)