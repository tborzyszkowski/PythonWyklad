from django.contrib import admin
from Question.models import *

class CategoryDisplay(admin.ModelAdmin):
    list_display = ('name', 'countReferences' )

class QuestionDisplay(admin.ModelAdmin):
    list_display = ('title', 'author', 'askDate', 'getRating', 'getViews')

class AnswerDisplay(admin.ModelAdmin):
    list_display = ('author', 'answerDate', 'getRating')

class VoteDisplay(admin.ModelAdmin):
    list_display = ('user', 'date', 'useragent', 'ip', 'vote')

class ViewDisplay(admin.ModelAdmin):
    list_display = ('user', 'date', 'useragent', 'ip')

admin.site.register(Category, CategoryDisplay)
admin.site.register(Question, QuestionDisplay)
admin.site.register(Answer, AnswerDisplay)
admin.site.register(Vote, VoteDisplay)
admin.site.register(View, ViewDisplay)