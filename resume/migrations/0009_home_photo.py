# Generated by Django 3.2.23 on 2023-12-15 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_auto_20231215_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='photo',
            field=models.ImageField(default='uploads/projects/photo.jpg', upload_to='uploads/projects'),
        ),
    ]