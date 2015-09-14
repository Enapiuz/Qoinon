# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0027_auto_20150726_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faucet',
            name='create_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2015, 7, 26, 17, 33, 29, 790303, tzinfo=utc)),
        ),
    ]
