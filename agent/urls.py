from django.urls import path, include

from agent.views import ProductFrontendAPIView, ProductBackendAPIView

urlpatterns = [
    path('', include('common.urls')),
    path('products/frontend', ProductFrontendAPIView.as_view()),
    path('products/backend', ProductBackendAPIView.as_view()),
    ]