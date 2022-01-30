from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now, localtime
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
  title = models.CharField(max_length=250)
  content = RichTextField(blank=True, null=True)
  thumbnail_image = models.ImageField(default='default.jpg', upload_to='thumbnails')

  date_posted = models.DateTimeField(auto_now=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('post-detail', kwargs={'pk': self.pk})