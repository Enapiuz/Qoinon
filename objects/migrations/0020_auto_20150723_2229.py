# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0019_auto_20150723_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faucet',
            name='minimum_withdraw',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='faucet',
            name='reward_max',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='faucet',
            name='reward_min',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='faucet',
            name='update_time',
            field=models.IntegerField(help_text='Cooldown в минутах'),
        ),
    ]
