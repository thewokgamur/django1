from django.urls import path
from . import views

app_news = 'core'
app_news = 'codexnews'

urlpatterns = [
    path('' , views.index, name='index'),
    path('index/' , views.index, name='index'),
    path('profile/' , views.profile, name='profile'),
]

