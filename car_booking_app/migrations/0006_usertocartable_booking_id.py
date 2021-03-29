# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_booking_app', '0005_remove_usertocartable_booking_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertocartable',
            name='booking_id',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
