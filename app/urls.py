from django.urls import path
from .views import HomeView , PostCreateView,PostUpdateView,delete,SearchResultsView

urlpatterns = [
    path('',HomeView.as_view(),name = 'stuHomeView'),
    path('post_create/',PostCreateView.as_view(),name = "stupost_create"),
    path('post_update/<int:pk>',PostUpdateView.as_view(),name = "stupost_update"),
    path('delete/<str:pk>',delete,name = 'studelete'),
    path('search/', SearchResultsView.as_view(), name='stusearch_results'),
]