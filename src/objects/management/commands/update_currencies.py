from django.core.management.base import BaseCommand, CommandError
import requests
from objects.models import Currency

class Command(BaseCommand):
    help = 'update currencies'

    def handle(self, *args, **options):
        self.update_btc()

        self.stdout.write('Everything done!')

    def update_btc(self):
        try:
            r = requests.get('https://blockchain.info/ru/ticker')
            if r.status_code == requests.codes.ok:
                value = float(r.json()['USD']['15m'])

                if value > 0:
                    btc = Currency.objects.filter(title_short_en='BTC').first()
                    btc.current_value = value
                    btc.save()
                    print('btc updated!')
            else:
                print('error update BTC')
        except Exception:
            print('error doing request')