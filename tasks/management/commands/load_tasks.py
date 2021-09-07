import json

from django.core.management.base import BaseCommand

from tasks.models import Question, Answer


class Command(BaseCommand):
    help = 'Load tasks from json file'

    def add_arguments(self, parser):
        parser.add_argument('tasks_json_filename', nargs=1)

    @staticmethod
    def parse_single_question(question_full_data):
        _some_id, question, *_ = question_full_data

        *_, answers_section = question_full_data
        answers_section = answers_section[0]
        _some_id, answers_metadata, *_ = answers_section

        answers = [answer for answer, *_ in answers_metadata]
        return question, answers

    @staticmethod
    def build_quiz_db(questions_full_data):
        quiz_db = []
        for single_question in questions_full_data:
            question, answers = Command.parse_single_question(single_question)
            quiz_db.append(
                {
                    'question': question,
                    'answers': answers,
                }
            )

        return quiz_db

    def handle(self, *args, **options):
        filename = options['tasks_json_filename'][0]

        with open(filename) as f:
            questions_full_data = json.load(f)

        quiz_db = self.build_quiz_db(questions_full_data)

        for task in quiz_db:
            question, _question_created = Question.objects.get_or_create(text=task['question'])

            for answer_text in task['answers']:
                answer, _answer_created = Answer.objects.get_or_create(
                    text=answer_text,
                    question=question,
                )
