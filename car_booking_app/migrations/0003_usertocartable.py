# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_booking_app', '0002_auto_20210327_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserToCarTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('booking_id', models.IntegerField(unique=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('car_id', models.ForeignKey(to='car_booking_app.car', unique=True)),
                ('user_id', models.ForeignKey(to='car_booking_app.UserProfile', unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
