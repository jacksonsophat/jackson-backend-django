from django.urls import path
from . import views

urlpatterns =[
    path('', views.newsOutlet),
    path('local-news/', views.localNews),
]
