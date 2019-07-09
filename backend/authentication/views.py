from django.utils.crypto import get_random_string
from rest_framework import viewsets, mixins, status, permissions, generics

from djoser import signals
from djoser.conf import settings as djoser_settings
from djoser.compat import get_user_email

from .models import User
from .serializers import UserSerializer


class UserViewSet(
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        permissions.IsAuthenticated
    )


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        password = get_random_string()
        user = serializer.save(password=password)

        context = {"user": user}
        to = [get_user_email(user)]
        
        if djoser_settings.SEND_ACTIVATION_EMAIL:
            djoser_settings.EMAIL.activation(self.request, context).send(to)
        elif djoser_settings.SEND_CONFIRMATION_EMAIL:
            context.update({"password": password})
