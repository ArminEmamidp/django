from django.urls import path

from . import views


app_name = 'api'
urlpatterns = [
    path('students/', views.StudentsApiView.as_view(), name='students'),
    path('students/create/', views.StudentCreateApiView.as_view(), name='student_create'),
    path('students/<id>/', views.StudentDetailApiView.as_view(), name='student_detail'),
    path('students/<id>/update/', views.StudentUpdateApiView.as_view(), name='student_update'),
    path('students/<id>/delete/', views.StudentDeleteApiView.as_view(), name='student_delete')
]