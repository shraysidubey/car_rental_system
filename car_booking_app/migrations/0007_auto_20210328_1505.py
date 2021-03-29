# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_booking_app', '0006_usertocartable_booking_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertocartable',
            name='booking_id',
            field=models.TextField(unique=True),
        ),
    ]
