from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class ThreadManager(models.Manager):
    def by_user(self, user):
        qs = self.get_queryset().filter(participants=user)
        return qs


class Thread(models.Model):
    participants = models.ManyToManyField(to=User, related_name="threads")
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ThreadManager()

    @property
    def room_group_name(self):
        return f'chat_{self.id}'

    def broadcast(self, msg=None):
        if msg is not None:
            broadcast_msg_to_chat(msg, group_name=self.room_group_name, user='admin')
            return True
        return False


class Message(models.Model):
    thread = models.ForeignKey(to=Thread, null=True, blank=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)