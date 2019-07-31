from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	model = Post

	def save_model(self, request, obj, form, change):
		obj.userId = request.user
		super().save_model(request, obj, form, change)
