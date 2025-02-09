from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer


class StudentsApiView(APIView):
	def get(self, request):
		students = Student.objects.all()
		serialized_students = StudentSerializer(students, many=True)

		return Response(serialized_students.data)


class StudentDetailApiView(APIView):
	def get(self, request, **kwargs):
		student = get_object_or_404(Student, id=kwargs['id'])
		serialized_student = StudentSerializer(student, many=False)

		return Response(serialized_student.data)


class StudentCreateApiView(APIView):
	def post(self, request):
		new_serialized_student = StudentSerializer(data=request.data, many=False)

		if new_serialized_student.is_valid():
			new_serialized_student.save()
		
		return Response(new_serialized_student.data)


class StudentUpdateApiView(APIView):
	def get(self, request, **kwargs):
		instance = get_object_or_404(Student, id=kwargs['id'])
		serialized_student = StudentSerializer(instance=instance, many=False)

		return Response(serialized_student.data)

	def post(self, request, **kwargs):
		instance = get_object_or_404(Student, id=kwargs['id'])
		serialized_student = StudentSerializer(instance=instance, data=request.data)

		if serialized_student.is_valid():
			serialized_student.save()
		
		return Response(serialized_student.data)


class StudentDeleteApiView(APIView):
	def get(self, request, **kwargs):
		student = get_object_or_404(Student, id=kwargs['id'])
		student.delete()

		return Response('The Student has been deleted successfully.')