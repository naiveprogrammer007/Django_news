import imp
from unicodedata import category
from wsgiref.util import request_uri
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

from newsapi import NewsApiClient

# Create your views here.

def newsapi_key():
    newsapi=NewsApiClient(api_key='ec84c3f1d9e8452b888ed528b2cc097b')
    return newsapi


def home_page(request):
    newsapi = newsapi_key()
    links=['bbc','verge','wired','vice'] 
    context={'urls':links} 
    return render(request,'landing_page.html',context)

def search_article(request):
   
    newsapi = newsapi_key()
    if request.method=="GET":
        searched=request.GET.get('q',None)
        all_articles = newsapi.get_everything(q=searched,sources='wired,vice-news, bbc-news')
        articles=all_articles['articles']
        paginator=Paginator(articles,20)
    
        page_number = request.GET.get('page')
        page=paginator.get_page(page_number)

        context={'articles':page,'searched':searched}   
        return render(request,'news/search.html',context)
    return render(request,'news/search.html',context)



def bbc_news(request):
    newsapi = newsapi_key()
    all_articles = newsapi.get_everything(sources='bbc-news')
    articles=all_articles['articles']
    
    paginator=Paginator(articles,20)
    
    page_number = request.GET.get('page')
    page=paginator.get_page(page_number)
    context={'articles':page}
    
    return render(request,"news/articles.html",context)

def verge_news(request):
    newsapi = newsapi_key()
    
    all_articles = newsapi.get_everything(sources='the-verge')
    articles=all_articles['articles']
   
    paginator=Paginator(articles,20)
    
    page_number = request.GET.get('page')
    page=paginator.get_page(page_number)
    context={'articles':page}
    
    return render(request,"news/articles.html",context)

def vice_news(request):
    newsapi = newsapi_key()
    all_articles = newsapi.get_everything(sources='vice-news')
    articles=all_articles['articles']
    
    paginator=Paginator(articles,20)
    
    page_number = request.GET.get('page')
    page=paginator.get_page(page_number)
    context={'articles':page}
    
    return render(request,"news/articles.html",context)

def wired_news(request):
    newsapi = newsapi_key()
    all_articles = newsapi.get_everything(sources='wired')
    articles=all_articles['articles']
    
    paginator=Paginator(articles,20)
    
    page_number = request.GET.get('page')
    page=paginator.get_page(page_number)
    context={'articles':page}
    
    return render(request,"news/articles.html",context)