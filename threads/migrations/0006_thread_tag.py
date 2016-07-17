# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0005_auto_20160716_0232'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='tag',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
    ]
