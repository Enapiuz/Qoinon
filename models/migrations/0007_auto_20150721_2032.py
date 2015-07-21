# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0006_auto_20150721_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='faucet',
            name='minimum_withdraw',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)], default=0),
        ),
        migrations.AlterField(
            model_name='faucet',
            name='reward_max',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], default=0),
        ),
        migrations.AlterField(
            model_name='faucet',
            name='reward_mid',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], default=0),
        ),
        migrations.AlterField(
            model_name='faucet',
            name='reward_min',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], default=0),
        ),
    ]
