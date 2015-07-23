# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0004_auto_20150720_2204'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaucetCategory',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title_en', models.CharField(max_length=300)),
                ('title_ru', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='faucet',
            name='reward_max',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='faucet',
            name='reward_mid',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='faucet',
            name='reward_min',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='faucet',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='faucet',
            name='update_time',
            field=models.TimeField(help_text='Cooldown'),
        ),
        migrations.AddField(
            model_name='faucet',
            name='category',
            field=models.ForeignKey(to='objects.FaucetCategory', null=True),
        ),
    ]
