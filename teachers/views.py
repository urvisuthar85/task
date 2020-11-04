from django.shortcuts import render,redirect
from .models import Teacher,Subject,Gender
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from .forms import TeacherForm 
from django.db.models import Q


# Create your views here.

class HomeView(ListView):
    model = Teacher
    template_name = 'teachers/index.html'


class PostCreateView(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = "teachers/post_create.html"


class PostUpdateView(UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = "teachers/post_update.html"



def delete(request,pk):
    teacher = Teacher.objects.get(id=pk)
    if request.method == "POST":
        teacher.delete()
        return redirect('/teacher/')

    context = {'teacher': teacher }
    return render(request,'teachers/delete.html',context)


