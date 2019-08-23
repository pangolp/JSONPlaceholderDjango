from django.urls import include, path
from rest_framework import routers

from .views import (
	GeoViewSet, AddressViewSet, CompanyViewSet,
	UserViewSet, TodoViewSet, PostViewSet,
	CommentViewSet, AlbumViewSet, PhotoViewSet
)


router = routers.DefaultRouter()
router.register('geos', GeoViewSet)
router.register('addresses', AddressViewSet)
router.register('companies', CompanyViewSet)
router.register('users', UserViewSet)
router.register('todos', TodoViewSet)
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)
router.register('albums', AlbumViewSet)
router.register('photoes', PhotoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
