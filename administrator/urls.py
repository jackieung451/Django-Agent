from django.urls import path, include

from .views import AgentAPIView, ProductGenericAPIView, LinkAPIView

urlpatterns = [
    path('', include('common.urls')),
    path('agents', AgentAPIView.as_view()),
    path('products', ProductGenericAPIView.as_view()),
    path('products/<str:pk>', ProductGenericAPIView.as_view()),
    path('users/<str:pk>/links', LinkAPIView.as_view()),
]