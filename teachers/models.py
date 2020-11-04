from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse

# Create your models here.


class Gender(models.Model):
    gender = models.CharField(max_length=20)

    def __str__(self):
        return self.gender

class Subject(models.Model):
    subject = models.CharField(max_length=20)

    def __str__(self):
        return self.subject

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    school = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher_firstname = models.CharField(max_length=255)
    teacher_lastname = models.CharField(max_length=255)
    teacher_gender = models.ManyToManyField(Gender)
    teacher_profession = models.ManyToManyField(Subject)
    teacher_age = models.IntegerField(default=21)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.teacher_firstname 
    
    def get_absolute_url(self):
        return reverse("TeacherHomeView")