from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):

    # no need for author (because it's always myself)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True, null=True) # remove null atributte when erasing the database
    text = models.TextField()
    language = models.CharField(max_length=50, default='portuguese-br', blank=True) # portuguese, english, etc..
    created = models.DateTimeField(auto_now_add=True)
    posted = models.DateTimeField(blank=True, null=True)
    #modified?
    tag = models.ManyToManyField('Tags', related_name='posts', blank=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.date_posted = timezone.now() 
        self.save()

class Tags(models.Model):

    tag = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)



# field types: https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-types
