from django.shortcuts import render
from rest_framework import generics, status
from .models import Post
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer, CreatePostSerializer
from rest_framework.decorators import api_view




# def mood(request):
#     html = "<p>Mood</p>"
#     return HttpResponse(html)

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})





@api_view()
def getPosts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view()
def getPost(request,pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createPost(request):
    if request.method == 'POST':
        serializer = CreatePostSerializer(data=request.data)
        if serializer.is_valid():
            post = serializer.save()
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(PostSerializer(post).data, status=status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)


# class CreatePostView(generics.CreateAPIView):
#     serializer_class = CreatePostSerializer

#     def createPost(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)
#         # if serializer.is_valid():
#         #     content = serializer.data.get('content')
#         #     mood = serializer.data.get('mood')
#         #     post = Post(content=content, mood=mood)
#             # print(post)
#             # post.save()
#             # return Response(PostSerializer(post).data, status=status.HTTP_201_CREATED)
#         # return Response({'Bad Request':'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
#         return Response({'Bad Request':'Invalid data...'})
