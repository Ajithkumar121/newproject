from django.db import models

# Create your models here.
class place(models.Model):
    head=models.CharField(max_length=200)
    image=models.ImageField(upload_to="photo")
    desc=models.TextField()

    def __str__(self):
        return self.head

class Team(models.Model):
    head=models.CharField(max_length=200)
    image=models.ImageField(upload_to="photo")
    desc=models.TextField()

    def __str__(self):
        return self.head
