from django.urls import path
from .views import UserActivity, UserPointsData


urlpatterns = [
    path('user-activity/', UserActivity.as_view(), name='user-activity'),
    path('user-points/<int:user_id>', UserPointsData.as_view(), name='user-points'),
]
