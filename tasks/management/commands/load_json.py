import json

from django.core.management.base import BaseCommand

from tasks.models import Question, Answer


class Command(BaseCommand):
    help = 'Load tasks from json file'

    def add_arguments(self, parser):
        parser.add_argument('tasks_json_filename', nargs=1)

    def handle(self, *args, **options):
        filename = options['tasks_json_filename'][0]

        with open(filename) as f:
            quiz_db = json.load(f)

        for task in quiz_db:
            question, _question_created = Question.objects.get_or_create(text=task['question'])

            for answer_text in task['answers']:
                answer, _answer_created = Answer.objects.get_or_create(
                    text=answer_text,
                    question=question,
                )
