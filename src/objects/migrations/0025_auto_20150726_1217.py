# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0024_auto_20150725_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faucet',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 26, 12, 17, 38, 581996), blank=True),
        ),
    ]
