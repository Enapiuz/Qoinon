from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Importing faucets from csv'

    def handle(self, *args, **options):
        self.stdout.write('Hello world')