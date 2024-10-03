from django.urls import path

from .views import HomeView, BoardView
from .views_auth import RegisterView, LoginView, LogoutView, UserProfileView
from .views_tasks import TaskCreateView, TaskUpdateView, TaskCompleteView

app_name = 'todo'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('board/', BoardView.as_view(), name='board'),
    path('task/create/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/complete/', TaskCompleteView.as_view(), name='task_complete'),
    path('auth/userProfile/', UserProfileView.as_view(), name='user_profile'),
]