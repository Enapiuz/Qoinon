# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0029_auto_20150730_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='faucet',
            name='iframe_ready',
            field=models.BooleanField(default=True, help_text='Возможность работы в iframe'),
        ),
        migrations.AlterField(
            model_name='faucet',
            name='create_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2015, 8, 2, 11, 51, 47, 397713, tzinfo=utc)),
        ),
    ]
