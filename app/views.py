from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from .forms import StudentCreateUpdateForm

import requests
import json


def home(request):
	return render(request, 'base/index.html')


def students_view(request):
	students = requests.get('http://localhost:8000/api/students/').json()
	context = {'students': students}

	return render(request, 'students/students.html', context)


def student_detail_view(request, **kwargs):
	student = requests.get(f'http://localhost:8000/api/students/{kwargs['id']}/').json()
	context = {'student': student}

	return render(request, 'students/detail.html', context)


def student_delete_view(request, **kwargs):
	requests.get(f"http://localhost:8000/api/students/{kwargs['id']}/delete/")
	messages.success(request, 'The Student has been deleted successfully.', 'primary')

	return redirect('app:students')


class StudentUpdateView(View):
	template_name = 'students/update.html'
	form_class = StudentCreateUpdateForm

	def get(self, request, **kwargs):
		student = requests.get(f"http://localhost:8000/api/students/{kwargs['id']}/update/").json()
		form = self.form_class(initial=student)
		context = {'form':form, 'student': student}

		return render(request, self.template_name, context)

	def post(self, request, **kwargs):
		student_id = kwargs['id']
		form = self.form_class(request.POST)
		context = {'form': form}

		if form.is_valid():
			cd = form.cleaned_data
			student_data = json.dumps(cd)
			headers = {'content-type': 'application/json'}
			requests.post(f"http://localhost:8000/api/students/{student_id}/update/", data=student_data, headers=headers)
			messages.success(request, 'The Student has been updated successfully.', 'primary')

			return redirect('app:student_detail', student_id)
		return render(request, self.template_name, context)


class StudentCreateView(View):
	template_name = 'students/create.html'
	form_class = StudentCreateUpdateForm

	def get(self, request):
		form = self.form_class()
		context = {'form': form}

		return render(request, self.template_name, context)

	def post(self, request, **kwargs):
		form = self.form_class(request.POST)
		context = {'form':form}

		if form.is_valid():
			cd = form.cleaned_data
			student_data = json.dumps(cd)
			headers = {'content-type':'application/json'}
			requests.post('http://localhost:8000/api/students/create/', data=student_data, headers=headers)
			messages.success(request, 'The Student has been created successfully.', 'primary')

			return redirect('app:students')
		return render(request, self.template_name, context)