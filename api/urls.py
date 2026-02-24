from . import views
from django.urls import path

urlpatterns=[
    path('students/',views.Studentsview),
    path('students/<int:pk>/',views.studentDetailView),
]