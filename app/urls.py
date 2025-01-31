from django.urls import path
from . import views


app_name = 'app'
urlpatterns = [
	path('', views.home, name='home'),
    path('contact-us/', views.contact_us_view, name='contact_us'),
    
	path('languages/', views.languages_view, name='languages'),
    path('languages/<name>/', views.language_lessons_view, name='language_lessons'),
    path('languages/<name>/<id>/<slug>', views.LanguageLessonDetailView.as_view(), name='language_lesson_detail'),

    path('dictionaries/', views.dictionaries_view, name='dictionaries'),
    path('dictionaries/<language>/', views.dictionary_detail_view, name='dictionary_detail'),

    path('blog/', views.blog_view, name='blog'),
    path('blog/<id>/<slug>/', views.BlogDetailView.as_view(), name='blog_detail')
]