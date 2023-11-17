from django.urls import path
from . import views

app_news = 'isi'

urlpatterns = [
    path('mu/<int:id>' , views.mu, name='mu'),
    path('all/' , views.all, name='all'),
    path('search/' , views.search, name='search'),
]