from django import forms
from .models import Teacher,Gender,Subject
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        
