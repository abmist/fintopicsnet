# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20160412_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='stripe_id',
            field=models.CharField(default='', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='subscription_end',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
