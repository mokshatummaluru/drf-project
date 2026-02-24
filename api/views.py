from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
# Create your views here.
def Studentview(request):
    students=Student.objects.all()
    students_list=list(students.values())
    return JsonResponse(students_list, safe=False)
