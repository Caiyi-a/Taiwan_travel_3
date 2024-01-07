from django.db import models

# Create your models here.
class Comment(models.Model):
    projectName = models.CharField(max_length=255)
    article = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_photos/', blank=True, null=True)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.projectName}"
    
class User(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.username}"