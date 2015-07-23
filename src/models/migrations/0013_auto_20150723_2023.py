# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0012_auto_20150722_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faucet',
            name='meta_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='faucet',
            name='meta_title',
            field=models.CharField(help_text='Максимум 1024 символа', max_length=1024, blank=True),
        ),
        migrations.RemoveField(
            model_name='faucet',
            name='update_time',
        ),
        migrations.AddField(
            model_name='faucet',
            name='update_time',
            field=models.IntegerField(help_text='Cooldown', default=0),
        ),
        migrations.AlterField(
            model_name='faucet',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
