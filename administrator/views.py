from django.shortcuts import render
from rest_framework.views import APIView

from core.models import User


class AgentAPIView(APIView):
    def get(self, _):
        agents = User.objects.filter(is_agent=True)