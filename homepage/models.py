from django.db import models
import datetime

class ExecMember(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    graduation_year = models.CharField(max_length=4)
    majors = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.ImageField()
    sort_index = models.IntegerField()
    year_term_started = models.IntegerField()

    def __str__(self):
        return self.full_name

class Project(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    associated_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField()
    caption = models.TextField(default='', blank=True)

    def __str__(self):
        return 'Image for \'' + self.associated_project.title + '\''

#----------BLOG POSTS----------

class BlogPost(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    date = models.DateField()
    text = models.TextField(blank=True)

    def __str__(self):
        return self.title

class BlogPostImage(models.Model):
    associated_blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    image = models.ImageField()
    caption = models.TextField(default='', blank=True)

    def __str__(self):
        return 'Image for \'' + self.associated_blog_post.title + '\''

#----------EVENTS----------

class Event(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    location = models.CharField(max_length=500)
    date = models.DateField()
    time = models.TimeField(blank=True)
    end = models.TimeField(blank=True, null=True)
    display = models.IntegerField(default=1)

    def __str__(self):
        return self.title

class EventImage(models.Model):
    associated_event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = models.ImageField()
    caption = models.TextField(default='', blank=True)

    def __str__(self):
        return 'Image from \'' + self.associated_event.title + '\''
