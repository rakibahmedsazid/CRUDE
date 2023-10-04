from django.db import models

# Create your models here.
class Employes(models.Model):
    name=models.CharField(max_length=45)
    email=models.EmailField(max_length=45)
    address=models.TextField()
    phone=models.IntegerField()
    img=models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
