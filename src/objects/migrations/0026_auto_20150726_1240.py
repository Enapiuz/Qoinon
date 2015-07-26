# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0025_auto_20150726_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faucet',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 26, 12, 40, 39, 61564), blank=True),
        ),
        migrations.AlterField(
            model_name='faucet',
            name='title_en',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]
