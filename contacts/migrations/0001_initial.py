# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('mobile', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
    ]
