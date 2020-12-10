from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class New(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_creation = models.DateTimeField(default=timezone.now)
    tag = models.ManyToManyField(Tag, blank=True, null=True, related_name='tags')

    def __str__(self):
        return self.title


