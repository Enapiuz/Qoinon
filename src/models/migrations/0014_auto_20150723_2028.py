# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0013_auto_20150723_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faucet',
            name='update_time',
            field=models.IntegerField(help_text='Cooldown'),
        ),
    ]
