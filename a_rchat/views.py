from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .form import ChatMessageCreateForm
from .models import ChatGroup

@login_required
def chat_view(request):
    chat_group = get_object_or_404(ChatGroup, group_name="public")
    chat_messages = chat_group.chat_message.all()[:30]  # Adjusted attribute name
    form=ChatMessageCreateForm()
    
    if request.htmx:
        form=ChatMessageCreateForm(request.POST)
        if form.is_valid:
            message=form.save(commit=False)
            message.author=request.user
            message.group=chat_group
            message.save()
        
    context = {
        'chat_messages': chat_messages,
        
        'form':form
    }
    return render(request, 'a_rchat/chat.html', context)
