from django import forms
from django.contrib.auth.models import User
from car_booking_app.models import UserProfile, car, UserToCarTable


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone_number','alias')


class update_UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email',)


class CarForm(forms.ModelForm):

    class Meta:
        model = car
        fields = ('car_license_no','manufacturer', 'model_city', 'base_price', 'price_per_hour', 'security_deposite')


class UserToCarTableForm(forms.ModelForm):

    start_time = forms.CharField(widget=forms.DateTimeInput(
        attrs={
        'class':'form-control',
        'type':'datetime-local'
        }
    ))
    end_time = forms.CharField(widget=forms.DateTimeInput(
        attrs={
        'class':'form-control',
        'type':'datetime-local'
        }
    ))
    class Meta:
        model = UserToCarTable
        fields = ('start_time', 'end_time',)