from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва завдання")
    description = models.TextField(blank=True, verbose_name="Опис")
    is_completed = models.BooleanField(default=False, verbose_name="Виконано")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")

    def __str__(self):
        return self.title


class AppInfo(models.Model):
    description = models.TextField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class OnlineUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='online_status')
    channel_name = models.CharField(max_length=255)
    connected_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Online user'
        verbose_name_plural = 'Online users'

    def __str__(self):
        return f"{self.user.username} (Online)"