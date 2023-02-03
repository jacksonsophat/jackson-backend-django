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
    #City: Austin
    # AustinChronicle
    AustinChronicle = feedparser.parse("https://www.austinchronicle.com/gyrobase/rss/daily-news.xml")
    AustinChronicle_Entries = AustinChronicle.entries 
    for item in AustinChronicle_Entries:
        try:
            image = item['links'][1]['href']
        except:
            image = False
        news = {
            'station':'Austin Chronicle',
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
            # City = Houston
            # ABC Feed
            KTRK = feedparser.parse("https://abc13.com/feed/")
            KTRK_Entries = KTRK.entries    
            # KTRK_logo = '/images/projects/local-news/ktrk.png'
            for item in KTRK_Entries:
                time = item['published']
                try:
                    image = item['media_thumbnail'][0]['url']
                except:
                    image = False
                news = {
                'station':'ABC13',
                'title': item['title'],
                'summary': item['summary'],
                'link': item['link'],
                'published': time,
                'image': image
                }
                data.append(news)

            # KHOU
            KHOU = feedparser.parse("https://www.khou.com/feeds/syndication/rss/news/local")
            KHOU_Entries = KHOU.entries  
            # KHOU_logo = '/images/projects/local-news/khou.png'
            for item in KHOU_Entries:
                link = item['links'][0]['href']
                try:
                    image = item['links'][1]['href']
                except:
                    image = False
                
                news = {
                    'station':'KHOU',
                    'title': item['title'],
                    'summary': item['summary'],
                    'link': link,
                    'published': item['published'],
                    'image': image
                    }
                data.append(news)
            
            # NBC
            KPRC = feedparser.parse("https://www.click2houston.com/arc/outboundfeeds/rss/category/news/local/?outputType=xml&size=10")
            KPRC_Entries = KPRC.entries 
            # KPRC_logo ='/images/projects/local-news/kprc.png'
            for item in KPRC_Entries:
                # image = item['media_content'][0]['url']
                try:
                    image = item['media_content'][0]['url']
                except:
                    image = False
                news = {
                    'station':'KPRC',
                    'title': item['title'],
                    'summary': item['summary'],
                    'link': item['link'],
                    'published': item['published'],
                    'image': image
                    }
                data.append(news)   
        elif (select_city == 'austin'):
            #City: Austin
            # NBC
            KXAN = feedparser.parse("https://www.kxan.com/feed/")
            KXAN_Entries = KXAN.entries 
            for item in KXAN_Entries[:10]:
                # link = 

                try:
                    image = item['links'][1]['href']
                except:
                    image = False
                news = {
                    'station':'KXAN',
                    'title': item['title'],
                    'summary': item['summary'],
                    'link': item['link'],
                    'published': item['published'],
                    'image': image
                    }
                data.append(news)
            
            # KVUE
            KVUE = feedparser.parse("https://www.kvue.com/feeds/syndication/rss/news/local")
            KVUE_Entries = KVUE.entries 
            for item in KVUE_Entries[:10]:
                try:
                    image = item['links'][1]['href']
                except:
                    image = False
                news = {
                    'station':'KVUE',
                    'title': item['title'],
                    'summary': item['summary'],
                    'link': item['link'],
                    'published': item['published'],
                    'image': image
                    }
                data.append(news)
            
            # AustinChronicle
            AustinChronicle = feedparser.parse("https://www.austinchronicle.com/gyrobase/rss/daily-news.xml")
            AustinChronicle_Entries = AustinChronicle.entries 
            for item in AustinChronicle_Entries[:10]:
                try:
                    image = item['links'][1]['href']
                except:
                    image = False
                news = {
                    'station':'Austin Chronicle',
                    'title': item['title'],
                    'summary': item['summary'],
                    'link': item['link'],
                    'published': item['published'],
                    'image': image
                    }
                data.append(news)
    return Response(data)

