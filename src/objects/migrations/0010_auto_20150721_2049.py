# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0009_faucet_referral_percent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faucet',
            name='minimum_withdraw',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], default=0),
        ),
    ]
