# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0003_contactform'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='solved',
            field=models.BooleanField(default=False),
        ),
    ]
