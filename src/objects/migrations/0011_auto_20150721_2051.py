# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0010_auto_20150721_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faucet',
            name='image',
            field=models.ImageField(upload_to='faucets', default='#'),
        ),
    ]
