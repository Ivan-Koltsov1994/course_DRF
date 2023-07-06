from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from course.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(verbose_name='почта', unique=True)
    phone = models.CharField(max_length=35, verbose_name='номер телефона')
    city = models.CharField(max_length=100, verbose_name='город')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        unique_together = ('email', 'phone')
        ordering = ('email',)  # сортировка, '-email' - сортировка в обратном порядке

    def __str__(self):
        return f'{self.email} - {self.phone}: {self.city}'
