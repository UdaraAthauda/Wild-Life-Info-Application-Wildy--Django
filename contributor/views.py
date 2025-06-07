from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, UserProfileForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# cotributor signup view
def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
        else:
            return render(request, 'signup.html', context={'form':form})

    else:
        return render(request, 'signup.html', context={'form':SignUpForm()})


# contributor login view
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', context={'form':form})
        else:
            return render(request, 'login.html', context={'form':form})
    
    else:
        return render(request, 'login.html', context={'form':LoginForm()})


# contributor profile view
@login_required(login_url='user_login')
def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
        else:
            return render(request, 'profile.html', context={'form':form})
    else:
        form = UserProfileForm(instance=request.user)
        return render(request, 'profile.html', context={'form':form})


# change password
@login_required(login_url='user_login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            logout(request)
            return redirect('user_login')
        else:
            return render(request, 'change_password.html', context={'form':form})
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'change_password.html', context={'form':form})


# delete account
@login_required(login_url='user_login')
def delete_account(request):
    user = request.user
    user.delete()
    return redirect('user_logout')


# logout view
@login_required(login_url='user_login')
def user_logout(request):
    logout(request)
    return redirect('home')