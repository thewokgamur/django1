from django.urls import path
from . import views

app_news = 'codexnews'

urlpatterns = [
    path('trading/' , views.trading, name='trading'),
    path('category/' , views.category, name='category'),
    path('sport/' , views.sport, name='sport'),
    path('politik/' , views.politik, name='politik'),
    path('horror/' , views.horror, name='horror'),
]

