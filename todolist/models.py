"""Models"""
from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    """Perfil dos usuarios"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_pic = models.ImageField(upload_to='images/', default='images/default.png')

    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

    def thumbnail(self):
        """Thumbnail for Profile Pic"""
        return mark_safe('<img src="{url}" height="{height}"'.format(
            url=self.profile_pic.url,
            height=150,
        ))

class Category(models.Model):
    """Categorias para to-do list"""
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=10, default='#c70d27')

    class Meta:
        verbose_name = ("Categoria")
        verbose_name_plural = ("Categorias")

    def __str__(self):
        return self.name

class List(models.Model):
    """To-do List model"""
    title = models.CharField(max_length=300)
    content = models.TextField(blank=True)
    created_date = models.DateField(default=timezone.now)
    done_date = models.DateField(blank=True, null=True)
    due_date = models.DateField(default=timezone.now)
    category = models.ForeignKey('todolist.Category', on_delete=models.CASCADE, default='general')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = ("Tarefa")
        verbose_name_plural = ("Tarefas")

    def conclude(self):
        """Conclui a tarefa"""
        self.done_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    @property
    def is_past_due(self):
        """Verifica se a data para conclusão é menor que a data atual"""
        return date.today() > self.due_date
        