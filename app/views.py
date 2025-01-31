from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages

from .models import Language, Dictionary, Comment, BlogPost
from .forms import  CommentForm


# Home / Main
def home(request):
	template_name = 'base/index.html'
	return render(request, template_name)


# Contact-Us
def contact_us_view(request):
	template_name = 'base/contact-us.html'
	return render(request, template_name)


################################################################
# Section--> Language


# Languages
def languages_view(request):
	template_name = 'language/index.html'
	languages = Language.objects.all()
	context = {'languages' : languages}
	return render(request, template_name, context=context)


# Language-Lessons
def language_lessons_view(request, name):
	template_name = 'language/lessons.html'
	language = get_object_or_404(Language, name=name)
	lessons = language.lessons.all()
	context = {'language' : language, 'lessons' : lessons}
	return render(request, template_name, context=context)


# Language-Lesson-Detail
class LanguageLessonDetailView(View):
	template_name = 'language/lesson-detail.html'
	form_class = CommentForm
	
	def get(self, request, **kwargs):
		form = self.form_class()
		language = get_object_or_404(Language, name=kwargs['name'])
		lesson = language.lessons.get(id=kwargs['id'])
		comments = lesson.comments.filter(status=True)
		context = {'language' : language, 'lesson' : lesson, 'comments':comments, 'form' : form}
		return render(request, self.template_name, context=context)
	
	def post(self, request, **kwargs):
		form = self.form_class(request.POST)
		language = get_object_or_404(Language, name=kwargs['name'])
		lesson = language.lessons.get(id=kwargs['id'])
		context = {'language' : language, 'lesson' : lesson, 'form' : form}

		if form.is_valid():
			cd = form.cleaned_data
			Comment.objects.create(lesson=lesson, user_name=cd['user_name'], user_email=cd['user_email'], text=cd['text']).save()
			messages.success(request, 'The comment had been sent successfully.', 'primary')
			return redirect('app:language_lesson_detail', language.name, lesson.id)
		return render(request, self.template_name, context=context)


################################################################


################################################################
# Section--> Dictionary


# Dictionaries
def dictionaries_view(request):
	template_name = 'dictionary/index.html'
	dictionaries = Dictionary.objects.all()
	context = {'dictionaries' : dictionaries}
	return render(request, template_name, context=context)


# Dictionary-Detail
def dictionary_detail_view(request, language):
	template_name = 'dictionary/dictionary-detail.html'
	dictionary = get_object_or_404(Dictionary, language=language)
	context = {'dictionary' : dictionary}
	return render(request, template_name, context=context)


################################################################


################################################################
# Section--> Blog


# Blog
def blog_view(request):
	template_name = 'blog/index.html'
	blog_posts = BlogPost.objects.all()
	context = {'posts' : blog_posts}
	return render(request, template_name, context=context)


# Blog-Detail
class BlogDetailView(View):
	template_name = 'blog/detail.html'

	def get(self, request, **kwargs):
		blog_post = get_object_or_404(BlogPost, id=kwargs['id'], slug=kwargs['slug'])
		context = {'post' : blog_post}
		return render(request, self.template_name, context=context)


################################################################

