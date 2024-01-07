from django.contrib import admin
from .models import Comment, User

# Register your models here.
admin.site.register(Comment)

class UserAdmin(admin.ModelAdmin):
    list_display = ("username")

admin.site.register(User)