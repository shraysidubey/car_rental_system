from django.contrib import admin

from car_booking_app.models import UserProfile, car, UserToCarTable

admin.site.register(UserProfile)

admin.site.register(car)

admin.site.register(UserToCarTable)