from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Question, Option, ResultTip
import random

def index(request):
    return render(request, "index.html")

def register(request):
    return render(request, "register.html")
    
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz_list.html', {'quizzes': quizzes})

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.prefetch_related('options').all()
    
    # Shuffle options server-side:
    for q in questions:
        q.shuffled_options = list(q.options.all())
        random.shuffle(q.shuffled_options)

    if request.method == 'POST':
        answers = []
        for q in questions:
            answer = request.POST.get(f'question_{q.id}')
            answers.append(answer)

        counts = {'A': 0, 'B': 0, 'C': 0}
        for t in answers:
            if t in counts:
                counts[t] += 1

        result_type = max(counts, key=counts.get)
        possible_tips = ResultTip.objects.filter(quiz=quiz, type=result_type)
        selected_tip = random.choice(possible_tips)

        context = {
            'quiz': quiz,
            'result_type': result_type,
            'count': counts[result_type],
            'tip': selected_tip
        }
        return render(request, 'quiz/result.html', context)

    return render(request, 'quiz/quiz_detail.html', {'quiz': quiz, 'questions': questions})

def contact(request):
    return render(request, 'contact.html')








