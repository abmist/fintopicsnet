# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20160717_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='stripe_id',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='user',
            name='subscription_end',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
