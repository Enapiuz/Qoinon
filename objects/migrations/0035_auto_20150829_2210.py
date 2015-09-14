# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0034_auto_20150823_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faucet',
            name='create_date',
            field=models.DateTimeField(blank=True, default=timezone.now()),
        ),
    ]
