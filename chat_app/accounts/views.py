from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .forms import RegisterForm, LoginForm
from .models import UserProfile
from chat.models import ChatModel
from subscribers.models import SubscribeModel

def register_view(request):
    form = RegisterForm(request.POST or None)
    users = User.objects.all()
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = User.objects.create_user(username, email, password, is_staff=False)
        user.save()
        profile = UserProfile(profile=user)
        profile.save()
        return redirect('/')
    return render(request, 'accounts/registr_form.html', {'form': form, 'users': users})

def login_view(request):
    form = LoginForm(request.POST or None)
    users = User.objects.all()
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            return redirect('login/')
    return render(request, 'accounts/login_form.html', {'form': form, 'users': users})

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def profile_view(request):
    profile = request.user
    user_msgs = ChatModel.objects.filter(user=profile)
    friendly_list = SubscribeModel.objects.filter(self_user=profile)
    return render(request, 'accounts/profile.html', {'profile': profile, 'user_msgs': user_msgs, 'friendly_list': friendly_list})

# def mainpage(request):
#     return HttpResponse(f'<h1>main page</h1>')