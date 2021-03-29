# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_booking_app', '0003_usertocartable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertocartable',
            name='car_id',
            field=models.ForeignKey(to='car_booking_app.car'),
        ),
        migrations.AlterField(
            model_name='usertocartable',
            name='user_id',
            field=models.ForeignKey(to='car_booking_app.UserProfile'),
        ),
    ]
