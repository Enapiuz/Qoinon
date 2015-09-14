# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0008_faucet_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='faucet',
            name='referral_percent',
            field=models.IntegerField(help_text='Сколько нам % с реферральной программы', default=0),
        ),
    ]
