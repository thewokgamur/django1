from django.shortcuts import render

# Create your views here.
def trading(request):
    return render(request, 'menu/trading.html')
def category(request):
    return render(request, 'menu/category.html')
def sport(request):
    return render(request, 'menu/Sport.html')
def politik(request):
    return render(request, 'menu/politik.html')