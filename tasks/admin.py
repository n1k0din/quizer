from django.contrib import admin

from tasks.models import Question, Answer


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['short_text', 'is_correct', 'question_id', 'question_short_text']
    list_editable = ['is_correct']

    def short_text(self, obj):
        return obj.text[:50]

    def question_id(self, obj):
        return obj.question.id

    def question_short_text(self, obj):
        return obj.question.text[:150]


admin.site.register(Question)
admin.site.register(Answer, AnswerAdmin)
