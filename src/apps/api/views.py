from rest_framework import viewsets, filters

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


class GeoViewSet(viewsets.ModelViewSet):
	queryset = Geo.objects.all()
	serializer_class = GeoSerializer


class AddressViewSet(viewsets.ModelViewSet):
	queryset = Address.objects.all()
	serializer_class = AddressSerializer


class CompanyViewSet(viewsets.ModelViewSet):
	queryset = Company.objects.all()
	serializer_class = CompanySerializer


class UserViewSet(viewsets.ModelViewSet):
	search_fields = ['name']
	filter_backends = (filters.SearchFilter, )
	queryset = User.objects.all()
	serializer_class = UserSerializer


class TodoViewSet(viewsets.ModelViewSet):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer


class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer


class AlbumViewSet(viewsets.ModelViewSet):
	queryset = Album.objects.all()
	serializer_class = AlbumSerializer


class PhotoViewSet(viewsets.ModelViewSet):
	queryset = Photo.objects.all()
	serializer_class = PhotoSerializer
