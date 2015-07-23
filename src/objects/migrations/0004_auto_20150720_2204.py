# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0003_auto_20150720_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='faucet',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='faucet',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
