from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()

router.register('groups', GroupViewSet, basename='Group')
router.register('posts', PostViewSet, basename='Post')
router.register('follow', FollowViewSet, basename='Follower')
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='Comment'
)

urlpatterns = [
    path(r'v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls))
]