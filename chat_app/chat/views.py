from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ChatForm
from .models import ChatModel
from subscribers.models import SubscribeModel

def index_view(request):
    form = ChatForm(request.POST or None)
    if form.is_valid():
        text = form.cleaned_data.get('text')
        msg = ChatModel(user=request.user, text=text)
        msg.save()
        return HttpResponseRedirect('/')
    query_chat = ChatModel.objects.all()
    return render(request, 'chat/index.html', {'form': form, 'query_chat': query_chat})