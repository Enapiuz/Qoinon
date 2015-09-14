# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0004_contactform_solved'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaqCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title_en', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='faqitem',
            name='visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='faqitem',
            name='category',
            field=models.ForeignKey(to='front.FaqCategory', default=None, null=True),
        ),
    ]
