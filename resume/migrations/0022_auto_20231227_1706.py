# Generated by Django 3.2.23 on 2023-12-27 14:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0021_alter_blogs_blog_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Photo', models.ImageField(default='upload/work/work.jpg', upload_to='uploads/work')),
                ('Type_of_Work', models.CharField(max_length=100)),
                ('date', models.TimeField(default=datetime.datetime(2023, 12, 27, 14, 6, 25, 560349, tzinfo=utc))),
            ],
        ),
        migrations.AlterField(
            model_name='blogs',
            name='Blog_Date',
            field=models.DateField(default=datetime.datetime(2023, 12, 27, 14, 6, 25, 560349, tzinfo=utc)),
        ),
    ]