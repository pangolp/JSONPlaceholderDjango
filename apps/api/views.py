from rest_framework import generics
from .serializers import PostSerializer
from .models import Post


class PostList(generics.ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer


class PostDetail(generics.ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
