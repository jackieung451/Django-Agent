from django.core.management import BaseCommand
from django_redis import get_redis_connection

from core.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        con = get_redis_connection("default")

        agents = User.objects.filter(is_agent=True)

        for agent in agents:
            con.zadd('rankings', {agent.name: float(agent.revenue)})