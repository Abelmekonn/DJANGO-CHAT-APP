from django.urls import path
from .views import *

urlpatterns = [
    path('',chat_view,name="home"),
    path('chat/<username>',get_or_crate_chatroom,name='start-chat'),
    path('chat/<username>',chat_view,name='chatroom'),
    
]