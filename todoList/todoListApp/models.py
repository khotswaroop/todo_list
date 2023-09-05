from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    time=models.TimeField(auto_now_add=True,blank=True)
    images=models.ImageField(upload_to='media',null=True)

    def __str__(self):
        return self.title
    
class ExtendUser(User):
    PK_FIELD='password'
    USERNAME_FIELD='username'