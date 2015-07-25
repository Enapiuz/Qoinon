# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0022_auto_20150725_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='faucet',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 25, 15, 40, 58, 389803), blank=True),
        ),
    ]
