from django.urls import path
from . import views

app_news = 'core'

urlpatterns = [
    path('' , views.index, name='index')
]