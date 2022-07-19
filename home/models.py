from django.db import models


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True, blank=True)
    avatar = models.ImageField(null=True, blank=True)

    def __str__(self):
        return 'Message ' + self.name + ' (' + self.email + ')'