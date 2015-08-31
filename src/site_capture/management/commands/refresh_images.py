import os
import uuid
import subprocess
from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand, CommandError
from objects.models import Faucet

class Command(BaseCommand):
    help = 'Make screenshots for all faucets'

    def handle(self, *args, **options):
        dir = os.path.dirname(__file__)
        job_file = os.path.join(dir, '../../job.js')
        base_command = "phantomjs --ignore-ssl-errors=true " + job_file + " {site} {output_file}"
        faucets_images_root = os.path.join(settings.MEDIA_ROOT, 'faucets')

        faucets = Faucet.objects.all()
        position = 0

        for faucet in faucets:
            position += 1
            if "#" in faucet.image.name:
                self.stdout.write('processing %s' % faucet.title_en)
                self.stdout.write('there is {0} from {1} faucet'.format(position, faucets.count()))
                image_name = str(uuid.uuid4()) + '.png'
                image_path = os.path.join(faucets_images_root, image_name)

                command = base_command.format(site=faucet.real_href(), output_file=image_path)
                process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

                try:
                    output, errors = process.communicate(timeout=60)
                    faucet.image.name = 'faucets/%s' % image_name
                    faucet.save()
                except Exception as e:
                    print("\t\tException: %s" % e)
                    try:
                        process.kill()
                    except Exception as oloex:
                        print("\t\tException: %s" % oloex)

        self.stdout.write('Everything done!')
