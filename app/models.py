from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Gender(models.Model):
    gender = models.CharField(max_length=20)

    def __str__(self):
        return self.gender

class Subject(models.Model):
    subject = models.CharField(max_length=20)

    def __str__(self):
        return self.subject


class Student(models.Model):
    school = models.ForeignKey(User, on_delete=models.CASCADE)
    student_firstname = models.CharField(max_length=255)
    student_lastname = models.CharField(max_length=255)
    student_gender = models.ManyToManyField(Gender)
    student_subject = models.ManyToManyField(Subject)
    student_admission_date = models.DateField(default='2020-11-03')
    student_fees = models.IntegerField(default=500)


    def __str__(self):
        return self.student_firstname 
    
    def get_absolute_url(self):
        return reverse("stuHomeView")


