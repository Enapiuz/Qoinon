# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0002_auto_20150720_2137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='metakeyword',
            old_name='text',
            new_name='text_en',
        ),
        migrations.AddField(
            model_name='metakeyword',
            name='text_ru',
            field=models.CharField(max_length=300),
            preserve_default=False,
        ),
    ]
