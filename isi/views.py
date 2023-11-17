from django.shortcuts import render
from django.shortcuts import get_object_or_404
from core import models
from django.views.generic import ListView, DetailView
# Create your views here.
def all(request):
    berita = models.berita.objects.all()
    context = {'berita' : berita}
    return render(request, 'berita/all.html', context)
def mu(request, id):
    berita = get_object_or_404(models.berita,pk=id)
    context = {'berita' : berita}
    return render(request, 'berita/mu.html', context)

def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        berita = models.berita.objects.filter(judul__icontains=q)
    else :
        berita = models.berita.objects.all()
    context = {'berita' : berita}
    return render(request, 'berita/all.html', context)