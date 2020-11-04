from django.urls import path
from .views import * 

urlpatterns = [

    path('',HomeView.as_view(),name = 'TeacherHomeView'),
    path('post_create/',PostCreateView.as_view(),name = "post_create"),
    path('post_update/<int:pk>',PostUpdateView.as_view(),name = "post_update"),
    path('delete/<str:pk>',delete,name = 'delete'),
    

]