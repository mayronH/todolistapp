"""Models"""
from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    """Categorias para to-do list"""
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Categoria")
        verbose_name_plural = ("Categorias")

    def __str__(self):
        return self.name

class List(models.Model):
    """"To-do List model"""
    title = models.CharField(max_length=300)
    content = models.TextField(blank=True)
    created_date = models.DateField(default=timezone.now)
    done_date = models.DateField(blank=True, null=True)
    due_date = models.DateField(default=timezone.now)
    category = models.ForeignKey('todolist.Category', on_delete=models.CASCADE, default='general')

    def conclude(self):
        """Conclui a tarefa"""
        self.done_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        