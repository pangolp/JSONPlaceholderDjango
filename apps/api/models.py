from django.db import models


class Geo(models.Model):
	lat = models.FloatField()
	lng = models.FloatField()

	def __str__(self):
		return '(%s, %s)' % (self.lat, self.lng)


class Address(models.Model):
	street = models.CharField(max_length=100)
	suite = models.CharField(max_length=100)
	city = models.CharField(max_length=50)
	zipcode = models.CharField(max_length=50)
	geo = models.ForeignKey(Geo, on_delete=models.CASCADE, related_name='geoId')

	def __str__(self):
		return '%s' % (self.street)


class Company(models.Model):
	name = models.CharField(max_length=100)
	catchPhrase = models.CharField(max_length=100)
	bs = models.CharField(max_length=100)

	def __str__(self):
		return '%s' % (self.name)


class User(models.Model):
	name = models.CharField(max_length=100)
	username = models.CharField(max_length=50, unique=True)
	email = models.EmailField()
	address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='addressId')
	phone = models.CharField(max_length=50)
	website = models.URLField()
	company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='companyId')

	def __str__(self):
		return '%s' % (self.username)


class Post(models.Model):
	userId = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user', editable=False)
	title = models.CharField(max_length=100)
	body = models.TextField()

	def __str__(self):
		return '%s' % (self.title)


class Comment(models.Model):
	postId = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_post')
	name = models.CharField(max_length=100)
	email = models.EmailField()
	body = models.TextField()

	def __str__(self):
		return '%s' % (self.name)


class Album(models.Model):
	userId = models.ForeignKey(User, on_delete=models.CASCADE, related_name='album_user', editable=False)
	title = models.CharField(max_length=100)

	def __str__(self):
		return '%s' % (self.title)


class Photo(models.Model):
	albumId = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='albumId')
	title = models.CharField(max_length=100)
	url = models.URLField()
	thumbnailUrl = models.URLField()

	def __str__(self):
		return '%s' % (self.title)


CHOICES_COMPLETED = (
	('true','true'),
	('false','false'),
)


class Todo(models.Model):
	userId = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todo_user', editable=False)
	title = models.CharField(max_length=100)
	completed = models.CharField(max_length=5, choices=CHOICES_COMPLETED)

	def __str__(self):
		return '%s' % (self.title)
