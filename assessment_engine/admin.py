from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Standard)
class StandrardAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_on', 'updated_on','status']
    search_fields = ['name']

  
@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name','created_on','updated_on','status']
    search_fields = ['name']

@admin.register(models.QuestionBank)
class QuestionBankAdmin(admin.ModelAdmin):
    list_display = ['title','standard_name','subject_name','created_on','updated_on','status']
    search_fields = ['title']
    list_filter = ['standard', 'subject']

    def standard_name(self, question_bank):
        return question_bank.standard.name

    def subject_name(self,question_bank):
        return question_bank.subject.name


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question','question_bank_title','created_on','updated_on','status']
    search_fields = ['question']
    list_filter = ['question_bank']

    def question_bank_title(self, question):
        return question.question_bank.title

@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer','question_question','is_correct','created_on','updated_on','status']
    search_fields = ['answer']
    list_filter = ['question']

    def question_question(self, answer):
        return answer.question.question