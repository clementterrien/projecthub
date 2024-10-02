from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models.board import Board

User = get_user_model()


@receiver(post_save, sender=User)
def create_default_board(sender, instance, created, **kwargs) -> None:
    if created:
        Board.objects.create(user=instance, name=f"{instance.username}'s Default Board", default=True)


@receiver(post_save, sender=User)
def save_user_board(sender, instance, **kwargs) -> None:
    instance.boards.filter(default=True).first().save()


def __pass__():
    return
