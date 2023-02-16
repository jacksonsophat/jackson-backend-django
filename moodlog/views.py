from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mood(request):
    html = "<p>Mood</p>"
    return HttpResponse(html)
