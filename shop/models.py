from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = model.TextField(blank=true)
    image = models.ImageField(upload_to='category, blank')
    
    class Meta:
        ordering= ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'