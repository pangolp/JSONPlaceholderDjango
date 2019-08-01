from django.urls import include, path
from .views import (
	UserList,
	PostList, PostDetail
)


urlpatterns = [
	path('users/', UserList.as_view()),
	path('posts/', PostList.as_view()),
	path('post/<int:pk>/', PostDetail.as_view()),
]
