# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('tag', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('content', models.TextField(null=True, blank=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
