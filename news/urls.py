from django.urls import path
from .views import (bbc_news,verge_news,vice_news,wired_news,search_article)

app_name='news'
urlpatterns = [
    
    path('bbc/',bbc_news,name='bbc'),
    path('verge/',verge_news,name='verge'),
    path('vice/',vice_news,name='vice'),
    path('wired/',wired_news,name='wired'),
    path('',search_article,name='search-article')
    
]
