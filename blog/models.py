from django.db import models
from django.utils import timezone, text

# Create your models here.

class Category(models.Model):

    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = text.slugify(self.title)
        super().save(*args, **kwargs)
    


class Post(models.Model):
    DRAFT = 'Draft'
    PUBLISHED = 'Published'
    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    )
    # no need for author (because it's always myself)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    posted = models.DateTimeField(blank=True, null=True)
    tag = models.ManyToManyField('Tag', related_name='posts', blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='posts')
    status = models.CharField(max_length=20, default='Draft', choices=STATUS_CHOICES)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = text.slugify(self.title)
        # When published the posted date will be automatically filled
        if self.status == 'Published':
            self.posted = timezone.now()
        super().save(*args, **kwargs)


class Tag(models.Model):

    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = text.slugify(self.title)
        super().save(*args, **kwargs)  # Call the "real" save() method


# field types: https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-types
# https://docs.djangoproject.com/en/2.0/topics/db/models/#overriding-predefined-model-methods
# https://docs.djangoproject.com/en/2.0/ref/utils/#django.utils.text.slugify