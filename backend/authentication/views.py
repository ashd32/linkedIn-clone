from django.utils.crypto import get_random_string
from rest_framework import viewsets, mixins, status, permissions, generics

from djoser import signals
from djoser.conf import settings as djoser_settings
from djoser.compat import get_user_email

from .models import User
from .serializers import UserSerializer
from .permissions import AccountPermissions


class UserViewSet(
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet,
    mixins.ListModelMixin,
):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        AccountPermissions,
    )
