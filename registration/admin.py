from django.contrib import admin
from .models import Quiz, Question, Option, ResultTip

class OptionInline(admin.TabularInline):
    model = Option
    extra = 1

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1
    inlines = [OptionInline]

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(ResultTip)
