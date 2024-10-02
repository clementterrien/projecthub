from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Board(models.Model):
    name = models.CharField(max_length=100, default='Default Board')
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boards')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    default = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.user.username}'s Board"

    def save(self, *args, **kwargs) -> None:
        """ Ensure that only one board per user is marked as default."""
        if self.default:
            # Ensure no other board is marked as default for this user
            Board.objects.filter(user=self.user, default=True).update(default=False)

        super().save(*args, **kwargs)
