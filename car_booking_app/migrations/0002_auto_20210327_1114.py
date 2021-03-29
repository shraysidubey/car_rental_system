# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_booking_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('car_license_no', models.TextField(default=b'', unique=True, blank=True)),
                ('manufacturer', models.TextField()),
                ('model_city', models.TextField()),
                ('base_price', models.IntegerField(max_length=2000)),
                ('price_per_hour', models.FloatField(max_length=2000)),
                ('security_deposite', models.FloatField(max_length=2000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='alias',
            field=models.CharField(default=b'', unique=True, max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.IntegerField(max_length=12),
        ),
    ]
