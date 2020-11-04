from django.shortcuts import render,redirect
from .models import Student,Subject,Gender
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from .forms import StudentForm
from django.db.models import Q

# Create your views here.

class HomeView(ListView):
    model = Student
    template_name = 'student/index.html'


class PostCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "student/post_create.html"


class PostUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "student/post_update.html"



def delete(request,pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        student.delete()
        return redirect('/student/')

    context = {'student': student }
    return render(request,'student/delete.html',context)


class SearchResultsView(ListView):
    model = Student
    template_name = 'student/search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Student.objects.filter(
            Q(student_firstname=query)
        )
        return object_list
