# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0020_auto_20150723_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faucet',
            name='currency',
            field=models.ForeignKey(default=1, to='objects.Currency'),
        ),
    ]
