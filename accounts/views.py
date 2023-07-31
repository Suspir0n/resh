from django.shortcuts import render, redirect
from accounts.forms import LoginForms, SignupForms
from accounts.models import CustomUser
from django.contrib import auth
from django.contrib import messages

def login_view(request):
    form = LoginForms()
    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            name_or_email = form['name_or_email_login'].value()
            password = form['password'].value()

            if name_or_email in '@':
                username = auth.authenticate(
                    request,
                    email=name_or_email,
                    password=password,
                )
            else:
                username = auth.authenticate(
                    request,
                    username=name_or_email,
                    password=password,
                )

            if username is not None:
                auth.login(request, username)
                messages.success(request, f'{name_or_email} successfully logged in!')
                return redirect('home')
            else:
                messages.error(request, 'Error when logging in!')
                return redirect('login')

    return render(request, 'accounts/login.html', {'form': form})

def signup_view(request):
    form = SignupForms()

    if request.method == 'POST':
        form = SignupForms(request.POST)

        if form.is_valid():
            name = form['username_signup'].value()
            email = form['email'].value()
            password = form['password'].value()

            if CustomUser.objects.filter(username=name).exists():
                messages.error(request, 'User already exist')
                return redirect('signup')

            username = CustomUser.objects.create_user(
                username=name,
                email=email,
                password=password
            )
            username.save()
            messages.success(request, f'{name} successful registration')
            return redirect('login')

    return render(request, 'accounts/signup.html', {'form': form})

def logout_view(request):
    auth.logout(request)
    messages.success(request, 'Logout successful!')
    return redirect('login')

