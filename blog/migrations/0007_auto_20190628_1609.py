# Generated by Django 2.2.2 on 2019-06-28 10:39

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190628_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(verbose_name='Content'),
        ),
    ]
