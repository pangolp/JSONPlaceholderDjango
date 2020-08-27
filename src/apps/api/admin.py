from django.contrib import admin
from .models import (
	Geo, Address, Company, User, Todo,
	Post, Comment,
	Album, Photo
)


@admin.register(Geo)
class GeoAdmin(admin.ModelAdmin):
	model = Geo


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
	model = Address


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
	model = Company


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	model = User


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
	model = Todo


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	model = Post


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	model = Comment


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
	model = Album


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
	model = Photo
