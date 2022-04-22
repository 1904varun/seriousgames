from django.urls import path
from .views import UserActivity


urlpatterns = [
    path('user-activity/', UserActivity.as_view(), name='user-activity'),
]
