# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Captcha',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title_en', models.CharField(max_length=300)),
                ('title_ru', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title_short_en', models.CharField(max_length=50)),
                ('title_full_en', models.CharField(max_length=300)),
                ('title_short_ru', models.CharField(max_length=50)),
                ('title_full_ru', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Faucet',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('href', models.CharField(max_length=1024)),
                ('title_en', models.CharField(max_length=300)),
                ('title_ru', models.CharField(max_length=300)),
                ('update_time', models.DateTimeField(help_text='Дата обновления, обновляется автоматически')),
                ('visible', models.BooleanField(default=False)),
                ('now_pays', models.BooleanField(default=True)),
                ('malfunction', models.BooleanField(default=False)),
                ('meta_title', models.CharField(help_text='Максимум 1024 символа', max_length=1024)),
                ('meta_description', models.TextField()),
                ('captcha', models.ForeignKey(to='objects.Captcha')),
                ('currency', models.ForeignKey(to='objects.Currency')),
            ],
        ),
        migrations.CreateModel(
            name='MetaKeyword',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('text', models.CharField(max_length=300)),
            ],
        ),
        migrations.RenameField(
            model_name='wallet',
            old_name='title_eng',
            new_name='title_en',
        ),
        migrations.RenameField(
            model_name='wallet',
            old_name='title_rus',
            new_name='title_ru',
        ),
        migrations.RenameField(
            model_name='walletcategory',
            old_name='title_eng',
            new_name='title_en',
        ),
        migrations.RenameField(
            model_name='walletcategory',
            old_name='title_rus',
            new_name='title_ru',
        ),
        migrations.AlterField(
            model_name='wallet',
            name='min_withdraw',
            field=models.IntegerField(help_text='Минимальная сумма вывода'),
        ),
        migrations.AddField(
            model_name='faucet',
            name='meta_keywords',
            field=models.ManyToManyField(to='objects.MetaKeyword'),
        ),
    ]
