from django.urls import path
from . import views

from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
    # MyTokenObtainPairView,
)



urlpatterns =[
    # path('posts', PostsView.as_view()),
    # path('create-post', CreatePostView.as_view()),
    path('hello', views.hello_world),
    path('all-posts/', views.getPosts),
    path('post/<str:pk>', views.getPost),
    path('create-post/', views.createPost),

    # Authentication
    path('get-routes/', views.getRoutes),


    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
