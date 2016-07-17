# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0003_auto_20160716_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='description',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]
