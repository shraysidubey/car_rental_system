from django.conf.urls import patterns, url
from car_booking_app import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^restricted/', views.restricted, name='restricted'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^user/$', views.profile, name='profile'),
        url(r'^user/delete/$', views.delete_user, name='delete_user'),
        url(r'^car_details/$', views.car_details, name='car_details'),
        url(r'^car_booking/$', views.car_booking, name='car_booking'),
        url(r'^user_history/$', views.user_history, name='user_history'),
        url(r'^car_history/(?P<id>[\w\-]+)/$', views.car_history, name='car_history'),
        url(r'^list_of_all_cars/$', views.list_of_all_cars, name='list_of_all_cars'),
)