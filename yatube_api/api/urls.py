from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_v1 = DefaultRouter()

router_v1.register('groups', GroupViewSet, basename='Group')
router_v1.register('posts', PostViewSet, basename='Post')
router_v1.register('follow', FollowViewSet, basename='Follower')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='Comment'
)

urlpatterns = [
    path(r'v1/', include('djoser.urls.jwt')),
    path('v1/', include(router_v1.urls))
]
