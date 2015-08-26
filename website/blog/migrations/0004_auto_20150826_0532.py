# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='jdId',
            field=models.CharField(max_length=20, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='url',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
    ]
