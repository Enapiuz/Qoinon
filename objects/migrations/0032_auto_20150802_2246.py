# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0031_auto_20150802_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='faucet',
            name='best',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='faucet',
            name='top',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='faucet',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 19, 46, 9, 790979, tzinfo=utc), blank=True),
        ),
    ]
