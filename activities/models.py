from django.db import models

# Create your models here.
class Activity(models.Model):  
    activityname = models.CharField(max_length=100)
    activityinfo = models.CharField(max_length=255)
    activityspot = models.CharField(max_length=255)
    activityimage = models.ImageField(upload_to='activity_photos/', blank=True, null=True)
    
    def __str__(self):
        return f'{self.activityname}'