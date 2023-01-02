from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, blank=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    image = models.ImageField(upload_to="blog_images/")
