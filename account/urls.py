from django.urls import path

from .views import SignupPageView,Profile

urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='register'),
    path('profile/', Profile.as_view(), name='profile'),
]
