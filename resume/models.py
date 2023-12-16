from django.db import models


# Create your models here.
class home(models.Model):
    my_image = models.ImageField(upload_to="uploads/image")
    work_completed = models.IntegerField(default=0)
    Years_of_Experience = models.IntegerField(default=0)
    Total_Clients = models.IntegerField(default=0)
    Award_Won = models.IntegerField(default=0)


class project(models.Model):
    Project_Photo = models.ImageField(upload_to='uploads/projects', default='uploads/projects/photo.jpg')
    Project_Name = models.CharField(max_length=100, null=False, blank=False, default='project name')
    Project_Type = models.CharField(max_length=100, null=False, blank=False, default='project type')

    def __str__(self):
        return self.Project_Name
