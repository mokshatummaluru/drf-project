from . import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('employees',views.EmployeeViewset,basename='employee')
urlpatterns=[
    path('students/',views.Studentsview),
    path('students/<int:pk>/',views.studentDetailView),
    path('',include(router.urls))
    
]