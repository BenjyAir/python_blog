# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150826_0532'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='book',
            name='isJD',
            field=models.BooleanField(default=True),
        ),
    ]
