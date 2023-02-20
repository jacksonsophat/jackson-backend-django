from django.urls import path
from . import views
# from .views import PostsView, CreatePostView

urlpatterns =[
    # path('posts', PostsView.as_view()),
    # path('create-post', CreatePostView.as_view()),
    path('hello', views.hello_world),
    path('all-posts/', views.getPosts),
    path('post/<str:pk>', views.getPost),
    path('create-post/', views.createPost),
]
