from django.db import models

# Create your models here.

class Breed(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    country = models.CharField(max_length=255)
    is_official = models.BooleanField(default=True)

    date_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.name)


class Anime(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    director = models.CharField(max_length=255)
    release_date = models.DateField()
    score = models.PositiveSmallIntegerField(default=0)
    picture = models.ImageField()

    date_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.title)


class Website(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    owner = models.CharField(max_length=255)
    logo = models.ImageField()

    date_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.name)
