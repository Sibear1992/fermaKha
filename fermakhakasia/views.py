from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'fermakhakasia/index.html')

def about(request):
    return render(request, 'fermakhakasia/about.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно. Теперь вы можете войти на сайт.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'fermakhakasia/register.html', {'form': form})

def user_login(request):
    error_message = ''
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                error_message = 'Invalid username or password'
        else:
            error_message = 'Invalid username or password'
    else:
        form = AuthenticationForm()
    return render(request, 'fermakhakasia/login.html', {'form': form, 'error_message': error_message})

def user_logout(request):
    logout(request)
    return redirect('index')

def shop(request):
    return render(request, 'fermakhakasia/shop.html')

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'fermakhakasia/registration/signup.html'

# Create your views here.
