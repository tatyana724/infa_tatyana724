from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .forms import UsersForm
from .models import Users

def index(request):
    return render(request,'main/index.html')

def about(request):
    return render(request,'main/about.html')

def attractions(request):
    return render(request,'main/attractions.html')
def registration(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        # Проверка правильности email
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, 'Неправильный формат email')
            return redirect('registration')

        # Проверка совпадения пароля и подтверждения пароля
        if password != confirm_password:
                messages.error(request, 'Пароль и подтверждение пароля не совпадают')
                return redirect('registration')

        # Добавление нового пользователя в базу данных
        new_user = Users(email=email, password=password)
        new_user.save()

        messages.success(request, 'Пользователь зарегистрирован успешно')
        return redirect('/')

    return render(request, 'main/registration.html')

def user(request):
    return render(request,'main/user.html')

def route(request):
    return render(request,'main/route.html')