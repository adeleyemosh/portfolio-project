from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255, blank=False)
    pub_date = models.DateTimeField()
    body = models.TextField(blank=False)
    image = models.ImageField(upload_to="blog_images/")