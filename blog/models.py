from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):

    # no need for author (because it's always myself)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True, null=True) # remove null atributte when erasing the database
    text = models.TextField()
    language = models.CharField(max_length=50, default='portuguese-br', blank=True) # portuguese, english, etc..
    date_created = models.DateTimeField(auto_now_add=True)
    date_posted = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.date_posted = timezone.now() 
        self.save()

# field types: https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-types