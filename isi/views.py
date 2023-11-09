from django.shortcuts import render

# Create your views here.
def mu(request):
    return render(request, 'berita/mu.html')