from datetime import date, timedelta
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from .models import CustomUser, Appointment


class MyRegFrom(UserCreationForm):
    username = forms.CharField(label="Enter User Name", widget=forms.TextInput(
        attrs={
            'class': 'form-control main',
            'placeholder': 'User Name',
        }
    ))
    first_name = forms.CharField(label="Enter First Name", widget=forms.TextInput(
        attrs={
            'class': 'form-control main',
            'placeholder': 'First Name',
        }
    ))
    last_name = forms.CharField(label="Enter Last Name", widget=forms.TextInput(
        attrs={
            'class': 'form-control main',
            'placeholder': 'Last Name',
        }
    ))
    email = forms.CharField(label="Enter LastName", widget=forms.EmailInput(
        attrs={
            'class': 'form-control main',
            'placeholder': 'Email Id',
        }
    ))
    mobile = forms.CharField(label="Enter LastName", widget=forms.TextInput(
        attrs={
            'class': 'form-control main',
            'placeholder': 'Mobile Number',
        }
    ))
    age = forms.CharField(label="Enter your age*", widget=forms.TextInput(
        attrs={
            'class': 'form-control main',
            'placeholder': 'Type Age',
        }))
    gender = forms.CharField(label="Enter your age*", widget=forms.TextInput(
        attrs={
            'class': 'form-control main',
            'placeholder': 'Type Gender',
        }))
    password1 = forms.CharField(label="Enter your password*", widget=forms.PasswordInput(
        attrs={
            'class': 'form-control main',
            'placeholder': 'Enter The Password',
        }
    ))
    password2 = forms.CharField(label="Enter your confirm password*", widget=forms.PasswordInput(
        attrs={
            'class': 'form-control main',
            'placeholder': 'Retype The Password',
        }
    ))

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'mobile', 'age', 'gender']


class MyLogInFrm(AuthenticationForm):
    username = forms.CharField(label="Enter UserName", widget=forms.TextInput(
        attrs={
            'class': 'form-control main',
            'placeholder': 'User Name',
        }
    ))
    password = forms.CharField(label="Enter your password*", widget=forms.PasswordInput(
        attrs={
            'class': 'form-control main',
            'placeholder': 'Enter The Password',
        }
    ))


class ChangeProfileFrm(UserChangeForm):
    password = None
    username = None
    first_name = forms.CharField(label="Enter First Name", widget=forms.TextInput(
        attrs={
            'class': 'form-control main',
            'placeholder': 'First Name',
        }
    ))
    last_name = forms.CharField(label="Enter Last Name", widget=forms.TextInput(
        attrs={
            'class': 'form-control main',
            'placeholder': 'Last Name',
        }
    ))
    email = forms.CharField(label="Enter LastName", widget=forms.EmailInput(
        attrs={
            'class': 'form-control main',
            'placeholder': 'Email Id',
        }
    ))
    mobile = forms.CharField(label="Enter LastName", widget=forms.TextInput(
        attrs={
            'class': 'form-control main',
            'placeholder': 'Mobile Number',
        }
    ))
    age = forms.CharField(label="Enter your age*", widget=forms.TextInput(
        attrs={
            'class': 'form-control main',
            'placeholder': 'Type Age',
        }
    ))
    gender = forms.CharField(label="Enter your age*", widget=forms.TextInput(
        attrs={
            'class': 'form-control main',
            'placeholder': 'Type Gender',
        }
    ))

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'mobile', 'age', 'gender']


class DateInput(forms.DateInput):
    input_type = 'date'


class AppointmentForm(forms.ModelForm):
    app_fix_date = forms.DateField(label="Select Appointment date*", widget=DateInput(
        attrs={
            'class': 'form-control main',
            'placeholder': 'Select Appointment date',
        }
    ))

    def clean_app_fix_date(self):
        ad = self.cleaned_data['app_fix_date']
        td = date.today()
        fd = date.today() + timedelta(days=30)
        if ad == td:
            raise forms.ValidationError('Selected date may not be today')
        elif ad < td:
            raise forms.ValidationError('Selected date may not be previous day')
        elif ad > fd:
            raise forms.ValidationError('Selected date must be within 30 days from current date')
        return ad

    class Meta:
        model = Appointment
        fields = ['app_fix_date']


class MyPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['old_password', 'new_password1', 'new_password2']:
            self.fields[fieldname].widget.attrs = {'class': 'form-control main'}
