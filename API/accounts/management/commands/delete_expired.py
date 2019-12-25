from django.core.management.base import BaseCommand, CommandError
from accounts.models import Codigo 
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Delete objects older than 10 minutes'

    def handle(self, *args, **options):
        Codigo.objects.filter(posting_date__lte=datetime.now()-timedelta(minutes=10)).delete()
        self.stdout.write('Deleted objects older than 10 minutes')