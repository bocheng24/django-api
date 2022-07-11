from math import prod
import json

# from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    
    data = {}
    product = Product.objects.all().order_by("?").first()

    if product:
        data = model_to_dict(product, fields = ['id', 'title', 'price'])
    else:
        data['message'] = 'Sorry, no product found!'
    
    return Response(data)
    