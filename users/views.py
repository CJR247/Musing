from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
# from .views import login, logout

# def login(request):
#     return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return render(request,'users/logout.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hey {username} your account is created!!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request,'users/register.html', {'form': form})


