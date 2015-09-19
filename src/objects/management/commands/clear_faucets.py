from django.core.management.base import BaseCommand, CommandError
import requests
from objects.models import Faucet

class Command(BaseCommand):
    help = 'Check alive faucets and set visible to False if not work'

    def handle(self, *args, **options):
        faucets = Faucet.objects.all()

        for faucet in faucets:
            error = False
            try:
                r = requests.get(faucet.href, timeout=5)
                if r.status_code != requests.codes.ok:
                    error = True
            except Exception:
                error = True

            if error:
                self.stdout.write('error - ' + faucet.href)
                faucet.visible = False
                faucet.save()
            else:
                self.stdout.write('ok - ' + faucet.href)

        self.stdout.write('Everything done!')
