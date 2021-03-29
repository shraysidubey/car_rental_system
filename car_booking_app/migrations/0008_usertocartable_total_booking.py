# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_booking_app', '0007_auto_20210328_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertocartable',
            name='total_booking',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
