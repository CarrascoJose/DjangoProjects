from django.db import models

# Create your models here.

class AppUser(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.username