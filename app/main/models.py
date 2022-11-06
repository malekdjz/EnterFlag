from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class User(AbstractUser):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    first_name = None
    last_name = None

    def __str__(self):
        return self.username



class Event(models.Model):
    name = models.CharField(max_length=20)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']

class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True,null=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']

class Challange(models.Model):
    name = models.CharField(max_length = 20)
    difficulty = models.CharField(max_length = 20)
    description = models.TextField(blank=True,null=True)
    link = models.URLField()
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    points = models.IntegerField()
    flag = models.CharField(max_length = 50)
    event = models.ForeignKey(Event,on_delete = models.CASCADE)
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['points','name']

class Team (models.Model):
    name = models.CharField(max_length = 20)
    solved = models.ManyToManyField(Challange)
    score = models.IntegerField()

    def __str__(self) -> str:
            return self.name

    class Meta:
        ordering = ['score','name']
        


class Participant(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    score = models.IntegerField()
    is_team_owner = models.BooleanField()
    team = models.ForeignKey(Team,blank=True,null=True,on_delete= models.PROTECT)

    def __str__(self) -> str:
        return self.username

    class Meta:
        ordering = ['username']

        

