from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/')

    # Добавляем related_name для связи с моделью Group
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
        verbose_name='groups',
        help_text='Группы, к которым принадлежит этот пользователь. Пользователь получает все разрешения, предоставленные каждой из его групп.',
    )

    # Добавляем related_name для связи с моделью Permission
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',
        blank=True,
        verbose_name='разрешения пользователя',
        help_text='Конкретные разрешения для этого пользователя.',
        related_query_name='custom_user',
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'


class ModeratorGroup(Group):
    class Meta:
        proxy = True

    def __str__(self):
        return 'Модераторы'