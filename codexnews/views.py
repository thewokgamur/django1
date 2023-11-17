from django.shortcuts import render
from django.shortcuts import get_object_or_404
from core import models
# Create your views here.
def trading(request):
    return render(request, 'menu/trading.html')
def category(request):
    return render(request, 'menu/category.html')
def sport(request):
    berita = models.berita.objects.filter(status='publish')
    kategori = models.kategori.objects.all()
    kategoriid = 1
    if kategoriid :
        berita = models.berita.objects.filter(kategoriid = kategoriid)
    else :
        berita = models.berita.objects.filter(status='publish')
    
    context = {'berita': berita, 'kategori' : kategori}

    return render(request, 'menu/Sport.html', context)

def politik(request):
    berita = models.berita.objects.filter(status='publish')
    kategori = models.kategori.objects.all()
    kategoriid = 2
    if kategoriid :
        berita = models.berita.objects.filter(kategoriid = kategoriid)
    else :
        berita = models.berita.objects.filter(status='publish')
    
    context = {'berita': berita, 'kategori' : kategori}

    return render(request, 'menu/politik.html', context)

def horror(request):
    berita = models.berita.objects.filter(status='publish')
    kategori = models.kategori.objects.all()
    kategoriid = 3
    if kategoriid :
        berita = models.berita.objects.filter(kategoriid = kategoriid)
    else :
        berita = models.berita.objects.filter(status='publish')
    
    context = {'berita': berita, 'kategori' : kategori}

    return render(request, 'menu/horror.html', context)