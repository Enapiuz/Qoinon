# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0014_auto_20150723_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='faucet',
            name='append_wallet',
            field=models.BooleanField(help_text='Автоматически подставлять в конец ссылки наш подходящий адрес кошелька', default=True),
        ),
        migrations.AlterField(
            model_name='faucet',
            name='href',
            field=models.CharField(max_length=1024),
        ),
    ]
