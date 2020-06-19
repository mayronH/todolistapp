"""Admin Panel"""
from django.contrib import admin
from django import forms
from .models import Category, List
from django.forms.widgets import TextInput

# Register your models here.

class ListAdmin(admin.ModelAdmin):
    """List Model on Admin"""
    list_display = ("title", "due_date", "created_date",)

class CategoryForm(forms.ModelForm):
    color = forms.CharField(widget=forms.TextInput(attrs={'type' : 'color'}))

class CategoryAdmin(admin.ModelAdmin):
    """Category Model on Admin"""
    form = CategoryForm
    list_display = ("name", "color")

admin.site.register(Category, CategoryAdmin)
admin.site.register(List, ListAdmin)
