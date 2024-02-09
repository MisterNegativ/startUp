from django.shortcuts import render
from .models import Advertisement

def home(request):
    advertisements = Advertisement.objects.all()
    return render(request, 'post/home.html', {'advertisements': advertisements})

def index(request):
    advertisements = Advertisement.objects.all()
    return render(request, 'post/index.html', {'advertisements': advertisements})