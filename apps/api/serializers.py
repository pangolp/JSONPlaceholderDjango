from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
	
	userId = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		model = Post
		fields = ('id', 'title', 'body', 'userId')
