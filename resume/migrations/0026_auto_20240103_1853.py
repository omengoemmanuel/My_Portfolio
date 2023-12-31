# Generated by Django 3.2.23 on 2024-01-03 15:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0025_auto_20231227_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='portfolios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Project_Photo1', models.ImageField(default='uploads/portfolio/portfoli.jpg', upload_to='uploads/portfolio')),
                ('Project_Photo2', models.ImageField(default='uploads/portfolio/portfoli.jpg', upload_to='uploads/portfolio')),
                ('Project_Photo3', models.ImageField(default='uploads/portfolio/portfoli.jpg', upload_to='uploads/portfolio')),
                ('Project_Category', models.CharField(max_length=100)),
                ('Project_Client', models.CharField(max_length=100)),
                ('Project_Date', models.DateField(default=datetime.datetime(2024, 1, 3, 15, 52, 59, 888854, tzinfo=utc))),
                ('project_Url', models.URLField()),
                ('Project_Description', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='blogs',
            name='Blog_Date',
            field=models.DateField(default=datetime.datetime(2024, 1, 3, 15, 52, 59, 887867, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='works',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 1, 3, 15, 52, 59, 887867, tzinfo=utc)),
        ),
    ]
