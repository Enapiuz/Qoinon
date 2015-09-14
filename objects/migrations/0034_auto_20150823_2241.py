# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0033_auto_20150810_0104'),
    ]

    operations = [
        migrations.AddField(
            model_name='faucet',
            name='help_text',
            field=models.TextField(blank=True),
        )
    ]
