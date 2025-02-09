from django.urls import path
from . import views


app_name = 'app'
urlpatterns = [
	path('', views.home, name='home'),
    
	path('students/', views.students_view, name='students'),
    path('students/create/', views.StudentCreateView.as_view(), name='student_create'),
    path('students/<id>/', views.student_detail_view, name='student_detail'),
    path('students/<id>/delete/', views.student_delete_view, name='student_delete'),
    path('students/<id>/update/', views.StudentUpdateView.as_view(), name='student_update')
]