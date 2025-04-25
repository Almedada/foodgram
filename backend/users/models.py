from django.contrib.auth.models import AbstractUser
from django.db import models
from foodgram_backend.constants import MAX_EMAIL_LENGTH, MAX_NAME_LENGTH


class MyUser(AbstractUser):
    avatar = models.ImageField(
        null=True,
        default=None
    )
    email = models.CharField(
        unique=True,
        max_length=MAX_EMAIL_LENGTH,
    )
    first_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
    )
    last_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']


User = MyUser


class Subscription(models.Model):
    subscriber = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
        verbose_name='Кто подписался'
    )
    subscribed_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscribers',
        verbose_name='На кого подписались'
    )

    class Meta:
        unique_together = ('subscriber', 'subscribed_to')
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'{self.subscriber} подписался на {self.subscribed_to}'
