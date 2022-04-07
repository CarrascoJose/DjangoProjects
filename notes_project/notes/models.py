from django.db import models

# Create your models here.

class AppUser(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'User'
    

class Note(models.Model):
    title = models.CharField(max_length=200)
    resume = models.TextField(max_length=200)
    body = models.TextField(max_length=400)
    publish_date = models.DateTimeField()
    image = models.ImageField()
    user = models.ForeignKey(AppUser,null=True,blank=True,on_delete=models.CASCADE)


    def __str__(self):
        return self.title