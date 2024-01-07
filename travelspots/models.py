from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.name}"
    
class Travelspot(models.Model):
    name = models.CharField(max_length=255)
    info = models.CharField(max_length=255, null=True)
    city = models.ForeignKey('City', related_name='travelspots', on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=100, null=True)
    link = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='travelspot_photos/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.name}"
    
class Hot(models.Model):
    hname = models.CharField(max_length=255)
    hinfo = models.CharField(max_length=255, null=True)
    hcity = models.CharField(max_length=255, null=True)
    haddress = models.CharField(max_length=100, null=True)
    hlink = models.CharField(max_length=100, null=True)
    himage = models.ImageField(upload_to='travelspot_photos/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.hname}"