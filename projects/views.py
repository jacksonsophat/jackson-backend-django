from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import feedparser
from dateutil import parser
import time
# from datetime import datetime
# Create your views here.

@api_view(['GET'])
def newsOutlet(request):
    data=[]
    KHOU = feedparser.parse("https://www.khou.com/feeds/syndication/rss/news/local")
    KHOU_Entries = KHOU.entries  
    for item in KHOU_Entries:
        title = item['title']  
        print(title)
        data.append(title)

    return Response(data)



















@api_view(['GET'])
def localNews(request):
    data=[]

    # ABC Feed
    ABC13 = feedparser.parse("https://abc13.com/feed/")
    ABC13_Entries = ABC13.entries    
    for item in ABC13_Entries:
        time = parser.parse(item['published'])
        time.strftime("%a-%m-%d-%Y %I:%M %p")
        try:
            image = item['media_thumbnail'][0]['url']
        except:
            image = False

        news = {
            'station':'ABC 13',
        'title': item['title'],
        'summary': item['summary'],
        'link': item['link'],
        'published': time,
        'image': image
        }
        data.append(news)
    # 
    return Response(data)

