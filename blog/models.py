from django.db import models
from django.utils import timezone, text

# Create your models here.

class Post(models.Model):

    # no need for author (because it's always myself)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True) # remove null atributte when erasing the database
    text = models.TextField()
    language = models.CharField(max_length=50, default='portuguese-br', blank=True) # portuguese, english, etc..
    created = models.DateTimeField(auto_now_add=True)
    posted = models.DateTimeField(blank=True, null=True)
    #modified?
    tag = models.ManyToManyField('Tag', related_name='posts', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = text.slugify(self.title)
        super().save(*args, **kwargs)

    def publish(self):
        self.posted = timezone.now() 
        self.save()

class Tag(models.Model):

    tag = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tag

    def save(self, *args, **kwargs):
        self.slug = text.slugify(self.tag)
        super().save(*args, **kwargs)  # Call the "real" save() method


# field types: https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-types
# https://docs.djangoproject.com/en/2.0/topics/db/models/#overriding-predefined-model-methods
# https://docs.djangoproject.com/en/2.0/ref/utils/#django.utils.text.slugify