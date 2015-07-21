# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0007_auto_20150721_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='faucet',
            name='image',
            field=models.ImageField(upload_to='', default='#'),
        ),
    ]
