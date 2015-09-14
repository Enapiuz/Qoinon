# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0017_auto_20150723_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faucet',
            name='title_ru',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
