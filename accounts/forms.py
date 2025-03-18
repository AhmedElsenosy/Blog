from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import *

class RegisterForm (UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterForm , self).__init__(*args, **kwargs)
        for field_name , field in self.fields.items():
            field.widget.attrs['class'] = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'

class LoginForm (forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter username' , 'class' : 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password' , 'class' : 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}))

class ChangePassForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(ChangePassForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({
            'placeholder': 'Enter old password',
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg '
                     'focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 '
                     'dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 '
                     'dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
        })
        self.fields['new_password1'].widget.attrs.update({
            'placeholder': 'Enter new password',
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg '
                     'focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 '
                     'dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 '
                     'dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
        })
        self.fields['new_password2'].widget.attrs.update({
            'placeholder': 'Confirm New password',
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg '
                     'focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 '
                     'dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 '
                     'dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
        })


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(ProfileForm , self).__init__(*args, **kwargs)
        for field_name , field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'