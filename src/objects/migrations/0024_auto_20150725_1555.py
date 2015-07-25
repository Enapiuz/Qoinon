# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0023_faucet_create_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurWallet',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('address', models.CharField(max_length=300)),
                ('comments', models.TextField(blank=True)),
                ('currency', models.ForeignKey(to='objects.Currency')),
            ],
        ),
        migrations.AlterField(
            model_name='faucet',
            name='create_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2015, 7, 25, 15, 55, 58, 727119)),
        ),
    ]
