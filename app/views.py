from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

def index(request):
    items = Item.objects.all()
    return HttpResponse('<br>'.join([item.name for item in items]))

