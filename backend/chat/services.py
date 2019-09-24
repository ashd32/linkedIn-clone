from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404

def get_last_10_messages(chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    return Thread.messages.order_by('-timestamp').all()[:10]

def get_current_chat(chat_id):
    return get_object_or_404(Chat, id=chat_id)

    