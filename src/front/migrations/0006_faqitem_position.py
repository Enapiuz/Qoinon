# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0005_auto_20150909_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='faqitem',
            name='position',
            field=models.IntegerField(default=0),
        ),
    ]
