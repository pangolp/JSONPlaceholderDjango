from django.urls import include, path
from .views import PostList, PostDetail


urlpatterns = [
	path('posts/', PostList.as_view()),
	path('post/<int:pk>/', PostDetail.as_view()),
]
