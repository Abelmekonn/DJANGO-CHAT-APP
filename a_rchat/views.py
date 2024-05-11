from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import ChatMessageCreateForm
from .models import ChatGroup

@login_required
def chat_view(request):
    chat_group = get_object_or_404(ChatGroup, group_name='public')
    chat_messages = chat_group.chat_message.all()[:30]  

    if request.htmx:
        form = ChatMessageCreateForm(request.POST)  # Pass POST data to form
        if form.is_valid():  # Check if form data is valid
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_group
            message.save()
            context={
                'message':message,
                'user':request.user
            }
            return render(request, 'a_rchat/partials/chat_message_p.html',context)
    else:
        form = ChatMessageCreateForm()  # If GET request, instantiate an empty form
    
    return render(request, 'a_rchat/chat.html', {'chat_messages': chat_messages, 'form': form})
