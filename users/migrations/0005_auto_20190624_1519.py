# Generated by Django 2.2.2 on 2019-06-24 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190619_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10, null=True),
        ),
    ]
