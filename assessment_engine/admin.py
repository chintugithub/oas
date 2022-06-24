from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Standard)
admin.site.register(models.Subject)
admin.site.register(models.QuestionBank)
admin.site.register(models.Question)
admin.site.register(models.Answer)