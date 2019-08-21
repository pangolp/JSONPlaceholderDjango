from django.urls import include, path
from .views import (
	GeoList, AddressList, CompanyList,
	UserList, TodoList, PostList,
	CommentList, AlbumList, PhotoList
)


urlpatterns = [
	path('geos/', GeoList.as_view()),
	path('addresses/', AddressList.as_view()),
	path('companies/', CompanyList.as_view()),
	path('users/', UserList.as_view()),
	path('todos/', TodoList.as_view()),
	path('posts/', PostList.as_view()),
	path('comments/', CommentList.as_view()),
	path('albums/', AlbumList.as_view()),
	path('photoes/', PhotoList.as_view()),
]
