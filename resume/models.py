from django.db import models
from django.utils import timezone


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


class referees(models.Model):
    Name = models.CharField(max_length=100)
    Brief_Message = models.CharField(max_length=300)
    Phone = models.IntegerField()
    Email = models.EmailField()
    Referee_Photo = models.ImageField(upload_to="uploads/referees", default="uploads/referees/pic.jpg")

    def __str__(self):
        return self.Name


class New_Messages(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField()
    subject = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.name


class servicess(models.Model):
    Web_Design_Description = models.CharField(max_length=200, null=False, blank=False)
    Web_Development_Description = models.CharField(max_length=200, null=False, blank=False)
    Photography_Description = models.CharField(max_length=200, null=False, blank=False)
    Network_Design_Description = models.CharField(max_length=200, null=False, blank=False)
    Graphic_Design_Description = models.CharField(max_length=200, null=False, blank=False)
    Marketig_Services_Description = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.Web_Design_Description


class blogs(models.Model):
    Blog_Photo = models.ImageField(upload_to="uploads/blogs", default="uploads/blogs/profile.jpg")
    Blog_Category = models.CharField(max_length=30, null=False, blank=False)
    blog_Title_Venue = models.CharField(max_length=100, null=False, blank=False)
    Blog_Description = models.CharField(max_length=100, null=False, blank=False)
    My_Photo = models.ImageField(upload_to="uploads/blogs", default="uploads/blogs/profile.jpg")
    My_Name = models.CharField(max_length=50, null=False, blank=False)
    Blog_Date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.blog_Title_Venue
