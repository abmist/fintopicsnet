# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160718_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postblog',
            name='image',
            field=models.ImageField(null=True, upload_to=b'static/images', blank=True),
        ),
    ]
