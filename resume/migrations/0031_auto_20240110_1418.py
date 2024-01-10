# Generated by Django 3.2.23 on 2024-01-10 11:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0030_auto_20240108_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='Date_Uploaded',
            field=models.DateField(default=datetime.datetime(2024, 1, 10, 11, 18, 44, 215212, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='Blog_Date',
            field=models.DateField(default=datetime.datetime(2024, 1, 10, 11, 18, 44, 216231, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='Photo',
            field=models.ImageField(default='uploads/feedback/feedback.png', upload_to='uploads/feedback'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 1, 10, 11, 18, 44, 218237, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='portfolios',
            name='Project_Date',
            field=models.DateField(default=datetime.datetime(2024, 1, 10, 11, 18, 44, 217239, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='works',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 1, 10, 11, 18, 44, 217239, tzinfo=utc)),
        ),
    ]
