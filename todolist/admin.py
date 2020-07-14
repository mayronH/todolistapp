"""Admin Panel"""
from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Category, List, Profile
from django.forms.widgets import TextInput

# Register your models here.

class ProfileInline(admin.StackedInline):
    """Profile inline"""
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'
    fields = ['bio', 'thumbnail', 'profile_pic']
    readonly_fields = ('thumbnail',)

class CustomUserAdmin(UserAdmin):
    """User with Profile Admin"""
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

class ListAdmin(admin.ModelAdmin):
    """List Model on Admin"""
    list_display = ("title", "due_date", "created_date",)

class CategoryForm(forms.ModelForm):
    """Color Pick for Category Model"""
    color = forms.CharField(widget=forms.TextInput(attrs={'type' : 'color'}))

class CategoryAdmin(admin.ModelAdmin):
    """Category Model on Admin"""
    form = CategoryForm
    list_display = ("name", "color")

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(List, ListAdmin)
