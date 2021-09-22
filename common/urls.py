from django.urls import path

from common.views import RegisterAPIView

urlpatterns = [
    path('register', RegisterAPIView.as_view())
]