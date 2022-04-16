from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router_v1 = DefaultRouter()

router_v1.register(r'v1/posts', PostViewSet, basename='posts')
router_v1.register(r'v1/groups', GroupViewSet, basename='groups')
router_v1.register(
    r'v1/posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')
router_v1.register(r'v1/follow', FollowViewSet, basename='follows')


urlpatterns = [
    path('', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
