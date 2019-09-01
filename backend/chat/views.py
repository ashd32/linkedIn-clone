from django.shortcuts import render
from rest_framework import viewsets
from .models import Thread, Message
from .serializers import ThreadSerializer


class ChatViewSet(viewsets.ModelViewSet):
    serializer_class = ThreadSerializer
    # TODO: permissions_classes

    def get_queryset(self):
        return(
            Thread.objects.by_user(self.request.user)
            .prefetch_related('participants')
        )

    # @action(detail=True, methods=['POST'])
    # def create(self, request):
    #     thread = Thread()
    #     thread.participants.add(self.request.user)
    #     thread.participants.add(
