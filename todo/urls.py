from django.urls import path

from .views import HomeView, BoardView
from .views_auth import RegisterView, LoginView, LogoutView

app_name = 'todo'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('board/', BoardView.as_view(), name='board'),
]