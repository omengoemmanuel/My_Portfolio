# Generated by Django 3.2.23 on 2023-12-26 09:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0020_auto_20231216_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='Blog_Date',
            field=models.DateField(default=datetime.datetime(2023, 12, 26, 9, 15, 9, 870938, tzinfo=utc)),
        ),
    ]
