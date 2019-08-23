from rest_framework import viewsets
from rest_framework.permissions import BasePermission, DjangoModelPermissions, SAFE_METHODS

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


class ReadOnly(BasePermission):
	def has_permission(self, request, view):
		return request.method in SAFE_METHODS


class GeoViewSet(viewsets.ModelViewSet):
	queryset = Geo.objects.all()
	serializer_class = GeoSerializer
	permission_classes = [ReadOnly]


class AddressViewSet(viewsets.ModelViewSet):
	queryset = Address.objects.all()
	serializer_class = AddressSerializer
	permission_classes = [ReadOnly]


class CompanyViewSet(viewsets.ModelViewSet):
	queryset = Company.objects.all()
	serializer_class = CompanySerializer
	permission_classes = [ReadOnly]


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [ReadOnly]


class TodoViewSet(viewsets.ModelViewSet):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer
	permission_classes = [ReadOnly]


class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = [DjangoModelPermissions|ReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	permission_classes = [ReadOnly]


class AlbumViewSet(viewsets.ModelViewSet):
	queryset = Album.objects.all()
	serializer_class = AlbumSerializer
	permission_classes = [ReadOnly]


class PhotoViewSet(viewsets.ModelViewSet):
	queryset = Photo.objects.all()
	serializer_class = PhotoSerializer
	permission_classes = [ReadOnly]
