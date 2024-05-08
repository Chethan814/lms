from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .forms import SignUpForm, LoginForm

def index(request):
    return render(request, 'index.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'User created successfully.'
            if user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user.is_customer:
                login(request, user)
                return redirect('customer')
            elif user.is_employee:
                login(request, user)
                return redirect('employee')
        else:
            msg = 'Error creating user. Please check the form.'
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})

def login_view(request):
    msg = None
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_admin:
                    return redirect('adminpage')
                elif user.is_customer:
                    return redirect('customer')
                elif user.is_employee:
                    return redirect('employee')
            else:
                msg = 'Invalid credentials. Please try again.'
        else:
            msg = 'Error validating form. Please try again.'
    return render(request, 'login.html', {'form': form, 'msg': msg}) 


def admin(request):
    return render(request, 'admin.html')


def customer(request):
    return render(request, 'customer.html')


def employee(request):
    return render(request, 'employee.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')
