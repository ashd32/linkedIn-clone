from .models import Friendship
from .signals import friendship_request_status_changed


def are_friends(user1, user2):
    return Friendship.objects.filter(
        user=user1, 
        friends__user=user2).exists()


def befriend(user1, user2):
    Friendship.objects.get(user=user1).friends.add(
                                            Friendship.objects.get(user=user2))

def unfriend(user1, user2):
    Friendship.objects.get(user=user1).friends.remove(
                                            Friendship.objects.get(user=user2))


def accept_friendship_request(friendship_request, user1, user2):
    befriend(user1, user2)
    friendship_request.accepted = True
    friendship_request.save()
    friendship_request_status_changed.send(
        sender=friendship_request,
        friendship_request=friendship_request,
        attributes=["accepted"] 
    )


def decline_friendship_requst(friendship_request):
    #signal
    friendship_request.delete()


def cancel_friendship_requset(friendship_request):
    #signal
    friendship_request.delete()