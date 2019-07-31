from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
	
	userId = serializers.PrimaryKeyRelatedField(read_only=True)

	class Meta:
		model = Post
		fields = ( 'userId', 'id', 'title', 'body')
