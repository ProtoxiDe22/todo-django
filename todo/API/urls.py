from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .api_views import UserViewSet, PersonalTaskViewSet, AllTaskViewSet

router = DefaultRouter()
router.register(r'tasks', PersonalTaskViewSet, basename='Task')

urlpatterns = [
    path('tasks/all/', AllTaskViewSet.as_view({'get': 'list'}), name='all-tasks'),
    path('users/', UserViewSet.as_view({'get': 'list'}), name='users'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]