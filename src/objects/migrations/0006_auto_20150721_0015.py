# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0005_auto_20150720_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faucet',
            name='category',
            field=models.ForeignKey(to='objects.FaucetCategory'),
        ),
    ]
