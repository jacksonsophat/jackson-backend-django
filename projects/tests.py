

from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import requests



def linkPreview(request):
    pageTitle = 'Social Media Link Preview'
    url_query = ''
    error = ''

    facebookDict = {}
    twitterDict = {}

    result = False
    if request.GET.get('url_query'):
        url_query = request.GET.get('url_query')
    try:
        if url_query:
            page = requests.get(url_query)
            page.status_code
            page.content
            soup = BeautifulSoup(page.content, 'html.parser')
            result = True

# facebook title
            if soup.find("meta", property="og:title"):
                try:
                    facebookTitle = soup.find(
                        "meta", property="og:title")["content"]
                except:
                    facebookTitle = "No meta title content"
            else:
                facebookTitle = 'No meta title given'

            # Facebook / LinkedIn
            # facebook URL
            if soup.find("meta", property="og:url"):
                try:
                    facebookUrl = soup.find(
                        "meta", property="og:url")["content"]
                except:
                    facebookUrl = "No meta URL content"

            else:
                facebookUrl = 'No meta URL given'

            # facebook description
            if soup.find("meta", property="og:description"):
                try:
                    facebookDescription = soup.find(
                        "meta", property="og:description")["content"]
                except:
                    facebookDescription = "No meta description content"

            else:
                facebookDescription = 'No meta description given'

            # facebook image
            if soup.find("meta", property="og:image"):
                try:
                    facebookImg = soup.find(
                        "meta", property="og:image")["content"]
                except:
                    facebookImg = ""

            else:
                facebookImg = ''

            # twitter title
            if soup.find("meta", attrs={"name": "twitter:title"}):
                try:
                    twitterTitle = soup.find(
                        "meta", attrs={"name": "twitter:title"})["content"]
                except:
                    twitterTitle = "No meta title content"
            else:
                twitterTitle = 'No meta title given'

            # twitter / LinkedIn
            # twitter URL
            if soup.find("meta", attrs={"name": "twitter:url"}):
                try:
                    twitterUrl = soup.find(
                        "meta", attrs={"name": "twitter:url"})["content"]
                except:
                    twitterUrl = "No meta URL content"

            else:
                twitterUrl = 'No meta URL given'

            # twitter description
            if soup.find("meta", attrs={"name": "twitter:description"}):
                try:
                    twitterDescription = soup.find(
                        "meta", attrs={"name": "twitter:description"})["content"]
                except:
                    twitterDescription = "No meta description content"

            else:
                twitterDescription = 'No meta description given'

            # twitter image
            if soup.find("meta", attrs={"name": "twitter:image"}):
                try:
                    twitterImg = soup.find(
                        "meta", attrs={"name": "twitter:image"})["content"]
                except:
                    twitterImg = ""

            else:
                twitterImg = ''

            facebookDict = {
                'image': facebookImg,
                'url': facebookUrl,
                'title': facebookTitle,
                'description': facebookDescription
            }

            twitterDict = {
                'image': twitterImg,
                'url': twitterUrl,
                'title': twitterTitle,
                'description': twitterDescription
            }

    except:
        error = 'Please check your URL'
    print(facebookDict)
    context = {'pageTitle': pageTitle, 'url_query': url_query,
               'error': error, 'result': result, 'facebookDict': facebookDict, 'twitterDict': twitterDict}
    return render(request, 'projects/link_preview.html', context)


# Password Generator
def passwordGenerator(request):
    pageTitle = 'Password Generator | Create your unique password for free'

    context = {'pageTitle': pageTitle, }
    return render(request, 'projects/password.html', context)
