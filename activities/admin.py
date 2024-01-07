from django.contrib import admin
from .models import Activity

# Register your models here.
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("activityname", "activityinfo", "activityspot", "activityimage")

admin.site.register(Activity)