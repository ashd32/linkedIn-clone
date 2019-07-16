from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
# from . import services
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

    def accept(self):
        Friendship.objects.befriend(self.from_user, self.to_user)
        self.accepted = True
        self.save()
        # Add signal
        # FriendshipRequest.objects.filter(from_user=user1,
        #                                  to_user=user2).delete()

    def decline(self):
        # signals.friendship_declined.send(sender=self)
        self.delete()

    def cancel(self):
        # signals.friendship_cancelled.send(sender=self)
        self.delete()

    
    
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