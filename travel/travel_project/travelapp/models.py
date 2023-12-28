from django.db import models

# Create your models here.
class travel(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    descr=models.TextField()
    def __str__(self):
        return self.name
class travel1(models.Model):
    heading=models.CharField(max_length=100)
    para=models.TextField()
    image=models.ImageField(upload_to='pics')