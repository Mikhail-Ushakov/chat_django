from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import SubscribeModel
@login_required
def subscribe_view(request, pk):
    if request.method == 'POST':
        user = get_object_or_404(User, id=pk)
        maybe_friendly = SubscribeModel.objects.filter(self_user=request.user, other_user=user)
        if user != request.user and not maybe_friendly:
            sub = SubscribeModel(self_user=request.user, other_user=user)
            sub.save()
        if maybe_friendly:
            messages.info(request, 'Пользователь уже в друзьях')
    return redirect('/')