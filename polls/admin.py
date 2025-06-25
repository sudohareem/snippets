from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):  # Or use StackedInline for vertical layout
    model = Choice
    extra = 3  # Number of empty choice forms to display

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
