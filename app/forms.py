from django import forms
from .models import Student
from .models import Student,Gender,Subject

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        