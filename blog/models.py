from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255, blank=False)
    pub_date = models.DateTimeField()
    body = models.TextField(blank=False)
    image = models.ImageField(upload_to="blog_images/")

    def __str__(self) -> str:
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_small(self):
        return self.pub_date.strftime("%b %e %Y")