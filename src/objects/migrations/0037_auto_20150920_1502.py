# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0036_auto_20150920_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='current_value',
            field=models.FloatField(default=0),
        )
    ]
