# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.CharField(null=True, max_length=100)),
                ('isJD', models.BooleanField()),
                ('jdId', models.CharField(null=True, max_length=20)),
                ('date', models.DateField()),
            ],
        ),
    ]
