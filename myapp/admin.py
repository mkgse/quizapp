from django.contrib import admin
from . models import quiz_model

# Register your models here.
@admin.register(quiz_model)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['id','question','option1','option2','option3','rightans']