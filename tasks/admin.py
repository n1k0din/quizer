from django.contrib import admin

from tasks.models import Question, Answer

admin.site.register(Question)
admin.site.register(Answer)
