from django.db import models
from taggit.managers import TaggableManager

class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

class Post(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    tags=TaggableManager()
    posted=models.DateField()

    class Meta:
        ordering=('-posted',)

    def get_absolute_url(self):
        return reverse('post', args=[self.id]) 

    def __str__(self):
        return f"{self.title}"
