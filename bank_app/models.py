from django.db import models
from django.urls import reverse


class Blog(models.Model):
    name = models.CharField(max_length=250)
    decsription = models.TextField()
    image = models.ImageField(upload_to='blog_images')

    def __str__(self):
        return self.name



class Branch(models.Model):
    branch_name = models.CharField(max_length=70, unique=True)
    link = models.URLField(unique=True, blank=True)
    def __str__(self):
        return self.branch_name

    # def get_url(self):
    #     return reverse('slug_path', args=[self.slug])


