from django.urls import path
from .views import UserActivity, UserPointsData, RewardsTable


urlpatterns = [
    path('user-activity/', UserActivity.as_view(), name='user-activity'),
    path('user-points/<int:user_id>', UserPointsData.as_view(), name='user-points'),
    path('rewards/', RewardsTable.as_view(), name='rewards'),
]
