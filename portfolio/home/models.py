from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    desc = models.TextField()

    def __str__(self):
        return self.name
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(max_length=200)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title