from django.shortcuts import render
from core.models import berita
from django.views.generic import ListView, DetailView
# Create your views here.
def index(request):
    return render(request, 'index.html')  
def indexa(request):
    return render(request, 'index1.html')  
def profile(request):
    return render(request, 'profile.html')  

