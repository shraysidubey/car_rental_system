from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    phone_number = models.IntegerField(max_length=12)
    alias = models.CharField(max_length=128, null=False,unique=True, default='')

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class car(models.Model):
    car_license_no = models.TextField(blank=True, unique=True, default='')
    manufacturer = models.TextField(null=False)
    model_city = models.TextField(null=False)
    base_price = models.IntegerField(max_length=2000)               #500
    price_per_hour = models.FloatField(max_length=2000)             #150
    security_deposite = models.FloatField(max_length=2000)          #1000

    def __unicode__(self):
        return self.car_license_no


class UserToCarTable(models.Model):
    user_id = models.ForeignKey(UserProfile, null=False)
    car_id = models.ForeignKey(car, null=False)
    booking_id = models.TextField(unique=True)
    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=False)
    total_booking_price = models.IntegerField(null=False, default=0)

    def __unicode__(self):
        return str('car_id:' +  str(self.car_id) + ' start_time: '+ str(self.start_time) + ' end_time: '+ str(self.end_time) )

