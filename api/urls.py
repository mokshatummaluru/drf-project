from . import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('employees',views.EmployeeViewset,basename='employee')
urlpatterns=[
    path('students/',views.Studentsview),
    path('students/<int:pk>/',views.studentDetailView),
    path('',include(router.urls)),
    path('blogs/',views.BlogsView.as_view()),
    path('comments/',views.CommentsView.as_view()),
    path('blogs/<int:pk>/',views.BlogDetail.as_view()),
    path('comments/<int:pk>/',views.CommentDetail.as_view()),
    
]