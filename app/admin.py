from django.contrib import admin

from .models import Language, Lesson, Comment, Dictionary, BlogPost


class LanguageAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'created', 'updated']
    list_filter = ['id', 'user', 'name', 'created', 'updated']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'language', 'title', 'created', 'updated']
    list_filter = ['id', 'user', 'language', 'title', 'created', 'updated']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'lesson', 'user_name', 'user_email', 'status', 'created']
    list_filter = ['id', 'lesson', 'user_name', 'user_email', 'status', 'created']


class DictionaryAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'language', 'created', 'updated']
    list_filter = ['id', 'user', 'language', 'created', 'updated']



class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'created', 'updated']
    list_filter = ['id', 'user', 'title', 'created', 'updated']



admin.site.register(Language, LanguageAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Dictionary, DictionaryAdmin)
admin.site.register(BlogPost, BlogPostAdmin)