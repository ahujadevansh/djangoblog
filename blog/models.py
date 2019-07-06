import os,datetime
from PIL import Image
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce import HTMLField

class Post(models.Model):

    def post_pic_path(self, filename):
        if filename != 'nopic.jpg':
            basefilename, file_extension = os.path.splitext(filename)
            randomstr = datetime.datetime.now().strftime('%d-%m-%Y_%I:%M:%S,%f')
            return 'post_pics/{authorid}/{basename}_{randomstring}{ext}'.format(
                authorid=self.author.id, basename=basefilename, randomstring=randomstr, ext=file_extension)

    title = models.CharField(max_length=1000)
    content = HTMLField('Content')
    date_posted = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_pic = models.ImageField(default='nopic.jpg', upload_to=post_pic_path)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_post_detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        img = Image.open(self.post_pic.path)

        if img.height > 400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.post_pic.path)
