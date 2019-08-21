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


class GeoList(generics.ListAPIView):
	queryset = Geo.objects.all()
	serializer_class = GeoSerializer


class AddressList(generics.ListAPIView):
	queryset = Address.objects.all()
	serializer_class = AddressSerializer


class CompanyList(generics.ListAPIView):
	queryset = Company.objects.all()
	serializer_class = CompanySerializer


class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class TodoList(generics.ListAPIView):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer


class PostList(generics.ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer


class CommentList(generics.ListAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer


class AlbumList(generics.ListAPIView):
	queryset = Album.objects.all()
	serializer_class = AlbumSerializer


class PhotoList(generics.ListAPIView):
	queryset = Photo.objects.all()
	serializer_class = PhotoSerializer
