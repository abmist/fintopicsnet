# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0002_auto_20160309_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='description',
            field=models.CharField(max_length=800),
        ),
    ]
