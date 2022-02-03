from django.contrib import admin
from .models import Choice, Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date","question_text"]
    inlines = [ChoiceInline]
    list_display = ("question_text","pub_date","was_published_recently")

admin.site.register(Question,QuestionAdmin)
