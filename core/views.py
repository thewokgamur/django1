from django.shortcuts import render
from django.shortcuts import get_object_or_404
from core import models
from core import models as mdl
# Create your views here.
def index(request):
    berita = models.beritaupdate1.objects.filter(status='publish')
    berita2 = mdl.berita.objects.filter(status='publish')
    kategori = mdl.kategori.objects.all()
    kategoriid = 1
    if kategoriid :
        berita2 = mdl.berita.objects.filter(kategoriid = kategoriid)
    else :
        berita2 = mdl.berita.objects.filter(status='publish')
    context = {'updates' : berita, 'berita' : berita2, 'kategori' : kategori}
    return render(request, 'index.html', context)  

def isi(request,id):
    berita = get_object_or_404(models.beritaupdate1,pk=id)
    berita2 = models.beritaupdate1.objects.filter(status='publish')
    context = {'berita' : berita, 'beritas' : berita2}
    return render(request, "isi.html", context)

def indexa(request):
    return render(request, 'index1.html')  
def profile(request):
    return render(request, 'profile.html')  

