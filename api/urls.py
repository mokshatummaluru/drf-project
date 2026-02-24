from . import views
from django.urls import path

urlpatterns=[
    path('students/',views.Studentsview),
    path('students/<int:pk>/',views.studentDetailView),
    path('employees/',views.Employees.as_view()),
    path('employees/<int:pk>/',views.EmployeeDetail.as_view()),
    
]