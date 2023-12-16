from django.urls import path
from .views import UserProfileView, UserPostsView, UpdateUserProfileView


app_name = "profiles"

urlpatterns = [
    path('user/<int:user_id>/', UserProfileView.as_view(), name='user-profile'),
    path('user/<int:user_id>/posts/', UserPostsView.as_view(), name='user-posts'),
    path('user/update-profile/', UpdateUserProfileView.as_view(), name='update-profile'),
]