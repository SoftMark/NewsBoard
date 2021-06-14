from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    link = models.TextField()
    date = models.DateTimeField()
    likes = models.IntegerField()
    unlikes = models.IntegerField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=100)
    text = models.TextField()

# Create your models here.
