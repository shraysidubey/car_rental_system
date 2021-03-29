# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_booking_app', '0008_usertocartable_total_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertocartable',
            name='total_booking',
            field=models.IntegerField(),
        ),
    ]
