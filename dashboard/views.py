from django.shortcuts import render, redirect
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def dashboard_view(request):
    user = CustomUser.objects.get(email=request.user)
    return render(request, 'dashboard/home.html', {'user': user})

@login_required(login_url='login')
def update_user_view(request, user_uuid):
    user = CustomUser.objects.get(uuid=user_uuid)
    user.username = request.POST.get('username')
    user.email = request.POST.get('email')
    if request.POST.get('password') != '*******':
        user.set_password(request.POST.get('password'))
        user.save()
        return redirect('login')

    user.save()
    return redirect('home')

@login_required(login_url='login')
def delete_user_view(request, user_uuid):
    user = CustomUser.objects.get(uuid=user_uuid)
    user.delete()
    return redirect('login')
