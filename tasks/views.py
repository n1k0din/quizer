from random import shuffle

from django.shortcuts import render

from tasks.models import Question, Answer


def index(request):
    prev_question = None
    correct_answers_for_prev_question = None

    if request.POST:
        correct_answer = set(request.session.get('correct'))
        many_answers = request.POST.getlist('posted_answer[]')
        if many_answers:
            posted_answer = set([int(answer) for answer in many_answers])
        elif request.POST.get('posted_answer'):
            posted_answer = {int(request.POST['posted_answer'])}
        else:
            posted_answer = None

        if posted_answer and correct_answer == posted_answer:
            request.session['score'] += 1
        else:
            request.session['score'] = 0
            prev_question = Question.objects.get(id=request.session['question'])
            correct_answers_for_prev_question = Answer.objects.filter(
                id__in=request.session['correct'],
            )

    if 'score' not in request.session:
        request.session['score'] = 0

    score = request.session['score']

    question = Question.objects.order_by('?').first()

    answers = question.question_answers.all()
    answers_ids_and_texts = [{'id': answer.id, 'text': answer.text} for answer in answers]
    shuffle(answers_ids_and_texts)

    correct_answers_ids = [answer.id for answer in question.question_answers.filter(is_correct=True)]
    is_radio = (len(correct_answers_ids) == 1)

    request.session['correct'] = correct_answers_ids
    request.session['question'] = question.id

    context = {
        'question': question,
        'answers': answers_ids_and_texts,
        'score': score,
        'is_radio': is_radio,
        'prev_question': prev_question,
        'correct_answers_for_prev_question': correct_answers_for_prev_question,
    }

    return render(request, 'index.html', context)
