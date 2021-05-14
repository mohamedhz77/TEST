from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager
from django.urls import reverse
from django.template.defaultfilters import slugify 

class Post(models.Model):
       STATUS_CHOICES = (
              ('draft','DRAFT'),
              ('published', 'Published'),
       )
       title   = models.CharField(max_length=250)
       author  = models.ForeignKey(User, on_delete=models.CASCADE)  
       body    = models.TextField()
       publish = models.DateTimeField(default = timezone.now)
       created = models.DateTimeField(auto_now_add=True)
       updated = models.DateTimeField(auto_now=True)
       status  = models.CharField(max_length = 10, choices = STATUS_CHOICES, default = 'draft')
       tags = TaggableManager() 

       slug    = models.SlugField(max_length=250, unique_for_date='publish')

       def get_absolute_url(self):
              return reverse('post_detail', kwargs={'slug': self.slug} )

       def save(self, *args, **kwargs): 
              if not self.slug:
                     self.slug = slugify(self.title)
              return super().save(*args, **kwargs)       

       class Meta:
              ordering = ('-publish',)

       def __str__(self):
              return self.title       