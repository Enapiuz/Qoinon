import os
import csv
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from objects.models import Faucet, Currency, FaucetCategory, Captcha

class Command(BaseCommand):
    help = 'Importing faucets from csv'

    def handle(self, *args, **options):
        dir = os.path.dirname(__file__)
        faucets_file = os.path.join(dir, '../../../../faucets.csv')

        with open(faucets_file) as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            first = True
            for row in reader:
                if first:
                    first = False
                    continue

                fc = Faucet()
                fc.currency = Currency.objects.get(pk=row[0])
                fc.title_en = row[1]
                fc.title_ru = row[1]
                fc.reward_min = row[2] if not row[2] == '' else None
                fc.reward_max = row[3] if not row[3] == '' else None
                fc.reward_mid = row[4] if not row[4] == '' else None
                fc.category = FaucetCategory.objects.get(pk=row[5])
                fc.update_time = row[6]
                fc.minimum_withdraw = row[7] if not row[7] == '' else None
                fc.href = row[8]
                fc.append_wallet = fc.href.endswith('?r=')
                fc.visible = not bool(row[9])
                fc.now_pays = bool(row[10])
                fc.captcha = Captcha.objects.get(pk=row[11])
                fc.referral_percent = row[12] if not row[12] == '' else None
                fc.create_date = timezone.now()
                fc.save()

        self.stdout.write('Everything done!')
