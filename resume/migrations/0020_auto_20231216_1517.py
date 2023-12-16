# Generated by Django 3.2.23 on 2023-12-16 12:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0019_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Blog_Photo', models.ImageField(default='uploads/blogs/profile.jpg', upload_to='uploads/blogs')),
                ('Blog_Category', models.CharField(max_length=30)),
                ('blog_Title_Venue', models.CharField(max_length=100)),
                ('Blog_Description', models.CharField(max_length=100)),
                ('My_Photo', models.ImageField(default='uploads/blogs/profile.jpg', upload_to='uploads/blogs')),
                ('My_Name', models.CharField(max_length=50)),
                ('Blog_Date', models.DateField(default=datetime.datetime(2023, 12, 16, 12, 17, 6, 668259, tzinfo=utc))),
            ],
        ),
        migrations.DeleteModel(
            name='blog',
        ),
    ]
