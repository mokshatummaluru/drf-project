from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def Studentview(request):
    students={
        "id":12,
        "name":"Moksha",
        "age":22,
    }
    return JsonResponse(students)
