from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import feedparser
from dateutil import parser
import time
from projects.components.local_news import local_news
# from .components import local_news




@api_view(['GET'])
def newsOutlet(request):
    data=[]
    ABC_8 = feedparser.parse("https://www.wfaa.com/feeds/syndication/rss/news/local")
    ABC_8_Entries = ABC_8.entries 
    for item in ABC_8_Entries:
        try:
            image = item['links'][1]['href']
        except:
            image = False
        news = {
            'station':'ABC 8',
            'title': item['title'],
            'summary': item['summary'],
            'link': item['link'],
            'published': item['published'],
            'image': image
            }
        data.append(news)

    return Response(data)



















@api_view(['GET'])
def localNews(request):
    select_city=''
    data=[]
    # select_city = 'houston'
    if request.query_params.get('select_city'):
        select_city = request.query_params.get('select_city')
        if (select_city == 'houston'):
            local_news.getHoustonNews(data)
        
        elif (select_city == 'austin'):
            local_news.getAustinNews(data)

        elif (select_city=='dallas'):
            local_news.getDallasNews(data)
    return Response(data)

