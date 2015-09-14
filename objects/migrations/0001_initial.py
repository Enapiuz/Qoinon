# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title_rus', models.CharField(max_length=300)),
                ('title_eng', models.CharField(max_length=300)),
                ('min_withdraw', models.IntegerField()),
                ('currencies_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WalletCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title_rus', models.CharField(max_length=300)),
                ('title_eng', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='wallet',
            name='category',
            field=models.ForeignKey(to='objects.WalletCategory'),
        ),
    ]
