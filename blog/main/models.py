from django.db import models


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=15)
    slug = models.CharField(max_length=100)
    time_stamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + ' by ' + self.author
