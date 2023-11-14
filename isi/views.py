from django.shortcuts import render
from django.shortcuts import get_object_or_404
from core import models
# Create your views here.
def all(request):
    berita = models.berita.objects.all()
    context = {'berita' : berita}
    return render(request, 'berita/all.html', context)
def mu(request):
    return render(request, 'berita/mu.html')
def get_object(self):
    return get_object_or_404(self.model, berita=self.request.berita)