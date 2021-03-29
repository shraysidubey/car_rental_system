# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_booking_app', '0010_auto_20210328_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertocartable',
            name='total_booking_price',
            field=models.IntegerField(default=0),
        ),
    ]
