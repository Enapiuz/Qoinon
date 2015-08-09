# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.core.validators
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0032_auto_20150802_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faucet',
            name='create_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2015, 8, 9, 22, 4, 30, 752304, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='faucet',
            name='minimum_withdraw',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='faucet',
            name='reward_max',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='faucet',
            name='reward_mid',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='faucet',
            name='reward_min',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
