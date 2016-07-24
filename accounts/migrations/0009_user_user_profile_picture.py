# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20160717_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_profile_picture',
            field=models.ImageField(upload_to='static/images/profiles/', null=True, verbose_name='profile picture', blank=True),
        ),
    ]
