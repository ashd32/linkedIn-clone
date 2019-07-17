from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from . import signals
import datetime


User = get_user_model()


class FriendshipRequest(models.Model):
    from_user = models.ForeignKey(
        to=User,
        related_name="invitations_from",
        on_delete=models.CASCADE,
    )
    to_user = models.ForeignKey(
        to=User,
        related_name="invitations_to",
        on_delete=models.CASCADE,
    )
    message = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(default=datetime.datetime.now, editable=False)
    accepted = models.BooleanField(default=False)

    class Meta:
        unique_together = (
            ('to_user', 'from_user'),
        )

    
    
class FriendshipManager(models.Manager):

    def friends_of(self, user, shuffle=False):
        queryset = User.objects.filter(friendship__friends__user=user)
        if shuffle:
            queryset = queryset.order_by('?')
        return queryset

        
class Friendship(models.Model):
    user = models.OneToOneField(to=User, related_name='friendship', on_delete=models.CASCADE)
    friends = models.ManyToManyField(to='self', symmetrical=True)
    objects = FriendshipManager()

    def friend_count(self):
        return self.friends.count()

   
@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        instance.friendship = Friendship.objects.create(user=instance)
    instance.friendship.save()


@receiver(signals.friendship_request_status_changed)
def friendship_request_сhanged(sender, friendship_request, attributes, **kwargs):
    if friendship_request.accepted == True:
        friendship_request.delete()
        print("deleted")