# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0021_auto_20150724_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faucet',
            name='category',
            field=models.ForeignKey(to='objects.FaucetCategory', default=4),
        ),
    ]
