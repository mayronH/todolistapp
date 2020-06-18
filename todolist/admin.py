"""Admin Panel"""
from django.contrib import admin
from .models import Category, List

# Register your models here.

class ListAdmin(admin.ModelAdmin):
    """List Model on Admin"""
    list_display = ("title", "due_date", "created_date",)

class CategoryAdmin(admin.ModelAdmin):
    """Category Model on Admin"""
    list_display = ("name", )

admin.site.register(Category, CategoryAdmin)
admin.site.register(List, ListAdmin)
