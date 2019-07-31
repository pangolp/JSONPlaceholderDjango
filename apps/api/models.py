from django.db import models
from django.contrib.auth.models import User


# POSTS
class Post(models.Model):
	userId = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userId', editable=False)
	title = models.CharField(max_length=100)
	body = models.TextField()

	def __str__(self):
		return '%s' % (self.title)
