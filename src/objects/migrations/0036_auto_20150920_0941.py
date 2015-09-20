# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0035_auto_20150829_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='display',
            field=models.BooleanField(default=True),
        )
    ]
