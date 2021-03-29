# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_booking_app', '0009_auto_20210328_1943'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usertocartable',
            old_name='total_booking',
            new_name='total_booking_price',
        ),
    ]
