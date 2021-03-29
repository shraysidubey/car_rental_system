# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_booking_app', '0004_auto_20210327_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertocartable',
            name='booking_id',
        ),
    ]
