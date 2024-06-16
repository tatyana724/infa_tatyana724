from django import forms
from .models import Users

class UsersForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ['email', 'password', 'confirm_password']

'''from .models import Users
from django.forms import ModelForm, TextInput

class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields =['email', 'password']

        widgest = {
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Ваш email'
            }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль'
            })
        }'''