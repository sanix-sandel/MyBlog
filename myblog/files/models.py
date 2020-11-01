from django.db import models
from taggit.managers import TaggableManager



class Category(models.Model):
    name=models.CharField(min=255)

    def __str__(self):
        return f"{self.name}"

# Create your models here.
class File(models.Model):
    title=models.CharField(min=255)
    book=models.FileField()
    tags=TaggableManager()
    posted=models.DateField()

    class Meta:
        ordering=('-posted')

    def get_absolute_url(self):
        return reverse('file', args=[self.id])    

    def __str__(self);
        return f"{self.title}"