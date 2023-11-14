from django.urls import path
from . import views

app_news = 'isi'

urlpatterns = [
    path('mu/' , views.mu, name='mu'),
    path('all/' , views.all, name='all'),
]