# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0011_auto_20150721_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faucet',
            name='href',
            field=models.CharField(max_length=1024, help_text='Для автоматической подстановки подходящего кошелька вписать WALLET в место, где он должен быть'),
        ),
    ]
