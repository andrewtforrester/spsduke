from django.db import models

class ExecMember(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    graduation_year = models.CharField(max_length=4)
    majors = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.ImageField()
    sort_index = models.IntegerField()

class Project(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)

class BlogPost(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    datetime_created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    image = models.ImageField()

class Event(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    date = models.DateField()
