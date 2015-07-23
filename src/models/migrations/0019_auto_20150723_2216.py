# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0018_auto_20150723_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faucet',
            name='minimum_withdraw',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='faucet',
            name='reward_max',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='faucet',
            name='reward_mid',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='faucet',
            name='reward_min',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
