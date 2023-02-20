from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','created','content','mood','post_status']




class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['content','mood','post_status']

