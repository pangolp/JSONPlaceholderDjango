from rest_framework import generics

from .serializers import (
	GeoSerializer, AddressSerializer, CompanySerializer,
	UserSerializer, TodoSerializer, PostSerializer,
	CommentSerializer, AlbumSerializer, PhotoSerializer
)

from .models import (
	Geo, Address, Company, User, Todo,
	Post, Comment,
	Album, Photo
)


class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class PostList(generics.ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer


class PostDetail(generics.ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
