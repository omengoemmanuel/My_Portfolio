# Generated by Django 3.2.23 on 2023-12-15 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20231215_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='photo',
            field=models.ImageField(upload_to='upload/myphotos'),
        ),
    ]
