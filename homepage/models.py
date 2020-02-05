from django.db import models
from markupfield.fields import MarkupField

class ExecMember(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    graduation_year = models.CharField(max_length=4)
    majors = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    description = MarkupField()
    picture = models.ImageField()
    sort_index = models.IntegerField()

    def __str__(self):
        return self.full_name

class Project(models.Model):
    title = models.CharField(max_length=500)
    description = MarkupField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    date = models.DateField()
    text = MarkupField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=500)
    description = MarkupField()
    date = models.DateField()

    def __str__(self):
        return self.title
