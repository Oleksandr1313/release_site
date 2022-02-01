from re import L
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from .models import Images

def index(request):
    images = Images.objects.all()
    return render(request, 'main/images_list.html', {"images" : images})