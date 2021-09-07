from django.db import models


class Question(models.Model):
    text = models.TextField('Текст вопроса', max_length=500)

    def __str__(self):
        return f'{self.text[:100]}...'


class Answer(models.Model):
    text = models.CharField('Текст ответа', max_length=200)

    question = models.ForeignKey(
        Question,
        related_name='question_answers',
        verbose_name='Вопрос',
        on_delete=models.CASCADE,
    )

    is_correct = models.BooleanField('Правильный?', default=False)

    def __str__(self):
        return f'{self.question.id}, {self.text}'
