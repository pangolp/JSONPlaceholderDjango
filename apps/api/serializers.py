from rest_framework import serializers
from .models import (
	Geo, Address, Company, User, Todo,
	Post, Comment,
	Album, Photo
)


class GeoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Geo
		fields = ('lat', 'lng')


class AddressSerializer(serializers.ModelSerializer):

	geo = GeoSerializer(read_only=True)

	class Meta:
		model = Address
		fields = ('street', 'suite', 'city', 'zipcode', 'geo')


class CompanySerializer(serializers.ModelSerializer):

	class Meta:
		model = Company
		fields = ('name', 'catchPhrase', 'bs')


class UserSerializer(serializers.ModelSerializer):
	
	address = AddressSerializer(read_only=True)
	company = CompanySerializer(read_only=True)

	class Meta:
		model = User
		fields = ('id', 'name', 'username', 'email', 'address', 'phone', 'website', 'company')


class TodoSerializer(serializers.ModelSerializer):

	userId = serializers.PrimaryKeyRelatedField(read_only=True)

	class Meta:
		model = Todo
		fields = ('userId', 'id', 'title', 'completed')


class PostSerializer(serializers.ModelSerializer):
	
	userId = serializers.PrimaryKeyRelatedField(read_only=True)

	class Meta:
		model = Post
		fields = ('userId', 'id', 'title', 'body')


class CommentSerializer(serializers.ModelSerializer):

	postId = serializers.PrimaryKeyRelatedField(read_only=True)

	class Meta:
		model = Comment
		fields = ('postId', 'id', 'name', 'email', 'body')


class AlbumSerializer(serializers.ModelSerializer):

	userId = serializers.PrimaryKeyRelatedField(read_only=True)

	class Meta:
		model = Album
		fields = ('userId', 'id', 'title')


class PhotoSerializer(serializers.ModelSerializer):

	albumId = serializers.PrimaryKeyRelatedField(read_only=True)

	class Meta:
		model = Photo
		fields = ('albumId', 'id', 'title', 'url', 'thumbnailUrl')
