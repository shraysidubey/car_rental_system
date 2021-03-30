from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from car_booking_app.forms import UserForm, UserProfileForm, update_UserForm, CarForm, UserToCarTableForm
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from car_booking_app.models import UserProfile, User, car, UserToCarTable
from django.contrib import messages
import random
import string
from datetime import datetime


def index(request):

    return render(request, 'car_booking_app/index.html')


def register(request):

    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
            'car_booking_app/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/car_booking_app/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your car_booking_app account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'car_booking_app/login.html', {})


def some_view(request):
    if not request.user.is_authenticated():
        return HttpResponse("You are logged in.")
    else:
        return HttpResponse("You are not logged in.")


@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/car_booking_app/')


@login_required
def profile(request):
    context_dict = {}                                                               #declare dictionary

    try:
        user_Profile = UserProfile.objects.get(user=request.user.id)                        #get object from UserProfile
        context_dict['user'] = user_Profile                                        #keu used in html and get the data
        if request.method == 'POST' and 'edit_submit' in request.POST:      #condition when post request is there and form is editsubmit
            form = update_UserForm(request.POST,instance=request.user)                                  #this use to fetch the form
            context_dict['form'] = form
            return render(request, 'car_booking_app/edit.html', context_dict)

        if request.method == 'POST' and 'profile_submit' in request.POST:
            form = update_UserForm(request.POST, instance=request.user)  # this use to fetch the formprint
            messages.success(request, 'Your details was successfully updated!')

            if form.is_valid():
                user_profile_obj = form.save(commit=False)
                user_profile_obj.save()

    except UserProfile.DoesNotExist:
        pass
    return render(request, 'car_booking_app/profile.html', context_dict)


@login_required
def delete_user(request):
    UserProfile.objects.get(user=request.user.id).delete()
    logout(request)
    return redirect('/car_booking_app')


def car_details(request):
    if not request.user.is_superuser:
        return HttpResponse('Unauthorized', status=401)
    context_dic = {}
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            details = form.save(commit=False)
            details.save()
            return index(request)    #take back to index page
        else:
            print form.errors
    else:
        form = CarForm()
        context_dic['form'] = form
    return render(request, 'car_booking_app/car_details.html', context_dic)


def get_available_cars(startTime, endTime):
    list_of_bookings_in_interval = UserToCarTable.objects.exclude(start_time__gte= startTime,start_time__lte=endTime)\
                                         .exclude(end_time__gte=startTime,end_time__lte=endTime)
    cars_which_are_booked = list(map(lambda x: x.car_id.id, list_of_bookings_in_interval))
    return car.objects.filter(id__in=cars_which_are_booked)


@login_required()
def car_booking(request):
    context_dict = {}

    if request.method == 'GET':
        context_dict['date_time_form'] = UserToCarTableForm()
    elif request.method == 'POST' and 'time_form' in request.POST:
        form_submitted = UserToCarTableForm(request.POST)
        date_range_details = form_submitted.save(commit=False)
        available_car_list = get_available_cars(date_range_details.start_time, date_range_details.end_time)
        context_dict['start_time'] = date_range_details.start_time.strftime("%Y-%m-%d %H:%M:%SZ")
        context_dict['end_time'] = date_range_details.end_time.strftime("%Y-%m-%d %H:%M:%SZ")
        context_dict['available_car_list'] = available_car_list
    elif request.method == 'POST' and 'car_booking_form' in request.POST:

        car_id = request.POST.get("car")
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")
        user_profile = UserProfile.objects.get(user_id=request.user.id)

        user_to_car_object = UserToCarTable()
        user_to_car_object.user_id = user_profile
        user_to_car_object.car_id = car.objects.get(id=car_id)
        user_to_car_object.start_time = start_time
        user_to_car_object.end_time = end_time
        user_to_car_object.booking_id = generate_random_string(20)
        user_to_car_object.total_booking_price = total_payment(user_to_car_object.start_time, user_to_car_object.end_time, car_id)
        user_to_car_object.save()
        context_dict["success_message"] = "Your booking is done with below details"
        context_dict['booking_object'] = user_to_car_object

    return render(request, 'car_booking_app/car_booking.html', context_dict)


def user_history(request):
    user_profile = UserProfile.objects.get(user=request.user.id)
    context_dict = {'user_history': UserToCarTable.objects.filter(user_id=user_profile)}
    return render(request, 'car_booking_app/user_history.html', context_dict)


def car_history(request, id):
    context_dict = {}
    try:
        car_object = car.objects.get(id=id)
        context_dict['car_object'] = car_object
        context_dict['car_history'] = UserToCarTable.objects.filter(car_id=car_object)
    except car.DoesNotExist:
        context_dict['car_not_found'] = True
    return render(request,'car_booking_app/car_history.html', context_dict)


def generate_random_string(len):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(len))


def calculate_car_price(start_time, end_time, price_per_hour, security_deposite, base_price):
    end_time_date_object = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%SZ")
    start_time_date_object = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%SZ")
    hours = (end_time_date_object - start_time_date_object).total_seconds()/3600.0
    return (hours*price_per_hour) + security_deposite + base_price


def total_payment(start_time, end_time, car_id):
    object_of_car = car.objects.get(id=car_id)
    return calculate_car_price(start_time, end_time, object_of_car.price_per_hour
                               , object_of_car.security_deposite,
                               object_of_car .base_price)

@login_required()
def list_of_all_cars(request):
    if not request.user.is_superuser:
        return HttpResponse('Unauthorized', status=401)
    else:
        context_dict = {}

        all_car_objects = car.objects.all()
        context_dict['all_car_objects'] = all_car_objects
        print "all_car_objects", all_car_objects
        return render(request,'car_booking_app/list_of_all_cars.html', context_dict)

