from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField()
    date_posted = models.DateField(auto_now_add = True)
    last_updated = models.DateField(auto_now = True)
    author = models.ForeignKey(User , on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_post_detail',kwargs = {'pk':self.pk})
