# Generated by Django 3.2.23 on 2023-12-16 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0016_new_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Web_Design_Description', models.CharField(max_length=200)),
                ('Web_Development_Description', models.CharField(max_length=200)),
                ('Photography_Description', models.CharField(max_length=200)),
                ('Network_Design_Description', models.CharField(max_length=200)),
                ('Graphic_Design_Description', models.CharField(max_length=200)),
                ('Marketig_Services_Description', models.CharField(max_length=200)),
            ],
        ),
    ]
