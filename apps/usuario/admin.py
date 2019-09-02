from django.contrib import admin
from .models import Generador


@admin.register(Generador)
class GeneradorAdmin(admin.ModelAdmin):
	list_display = ('get_user', 'get_last_name', 'get_first_name', 'get_email', 'telefono')

	def get_user(self, obj):
		return obj.user.username
	get_user.short_description = 'username'

	def get_first_name(self, obj):
		return obj.user.first_name
	get_first_name.short_description = 'nombre'

	def get_last_name(self, obj):
		return obj.user.last_name
	get_last_name.short_description = 'apellido'

	def get_email(self, obj):
		return obj.user.email
	get_email.short_description = 'email'
