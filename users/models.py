import os,datetime
from PIL import Image
from django.db import models
from django.contrib.auth.models import User
from django import forms

class Profile(models.Model):

    def profile_pic_path(self,filename):
        if(filename!='nopic.jpg'):
            basefilename, file_extension= os.path.splitext(filename)
            randomstr= datetime.datetime.now().strftime('%d-%m-%Y_%I:%M:%S,%f')
            return 'profile_pics/{userid}/{basename}_{randomstring}{ext}'.format(userid= self.user.id, basename= basefilename, randomstring= randomstr, ext= file_extension)


    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='nopic.jpg',upload_to=profile_pic_path)
    Date_Of_Birth = models.DateField(null=True)
    Address = models.TextField(null=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    Gender = models.CharField(null=True,max_length = 10,choices = [('Male','Male'),('Female','Female'),('Othet','Other')])

    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)

        if img.height > 300 or img.width >300 :
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

