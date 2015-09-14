# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0030_auto_20150802_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faucet',
            name='create_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2015, 8, 2, 12, 3, 34, 640776, tzinfo=utc)),
        ),
    ]
