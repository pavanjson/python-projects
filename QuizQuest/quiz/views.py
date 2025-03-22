# quiz/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Quiz, Question, Option, Score, TestAttempt
from .forms import QuizForm, SignUpForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
import json
import datetime

# Set the cooldown period (in hours) for retaking the quiz
COOLDOWN_HOURS = 24  # Change to 168 for one week, etc.

def home(request):
    return render(request, 'quiz/home.html')

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/quiz_list.html', {'quizzes': quizzes})

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)

    if request.method == 'POST':
        step = request.POST.get('step')
        if step == 'start':
            # Process email/mobile submission
            email = request.POST.get('email').strip()
            mobile = request.POST.get('mobile').strip()
            attempt_qs = TestAttempt.objects.filter(quiz=quiz, email=email, mobile=mobile)
            if attempt_qs.exists():
                attempt = attempt_qs.latest('date_taken')
                cooldown = datetime.timedelta(hours=COOLDOWN_HOURS)
                now = timezone.now()
                if now - attempt.date_taken < cooldown:
                    remaining = cooldown - (now - attempt.date_taken)
                    remaining_hours = remaining.seconds // 3600
                    remaining_minutes = (remaining.seconds % 3600) // 60
                    user_answers = json.loads(attempt.user_answers) if attempt.user_answers else {}
                    print(user_answers)
                    return render(request, 'quiz/quiz_already_taken.html', {
                        'quiz': quiz,
                        'message': "You have already taken this quiz with these details.",
                        'score': attempt.score,
                        'total': quiz.questions.count(),
                        'remaining': f"{remaining_hours} hours and {remaining_minutes} minutes",
                        'user_answers': user_answers,
                    })
            # Save details in session and reload page to display questions
            request.session['quiz_email'] = email
            request.session['quiz_mobile'] = mobile
            return redirect('quiz_detail', quiz_id=quiz.id)
        elif step == 'submit':
            # Process quiz submission
            email = request.session.get('quiz_email')
            mobile = request.session.get('quiz_mobile')
            if not email or not mobile:
                return redirect('quiz_detail', quiz_id=quiz.id)
            total = 0
            correct = 0
            user_answers = {}
            questions = quiz.questions.all().order_by('order')
            for question in questions:
                # Store answer with key as string
                selected_option = request.POST.get(str(question.id))
                user_answers[str(question.id)] = selected_option
                if selected_option:
                    option = Option.objects.get(id=selected_option)
                    total += 1
                    if option.is_correct:
                        correct += 1
            # Save the test attempt along with the user's answers as JSON
            TestAttempt.objects.create(
                quiz=quiz,
                email=email,
                mobile=mobile,
                score=correct,
                user_answers=json.dumps(user_answers)
            )
            # Clear session data related to quiz taking
            request.session.pop('quiz_email', None)
            request.session.pop('quiz_mobile', None)
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'score': correct, 'total': total})
            return render(request, 'quiz/score.html', {'score': correct, 'total': total})
    else:  # GET request
        email = request.session.get('quiz_email')
        mobile = request.session.get('quiz_mobile')
        if email and mobile:
            attempt_qs = TestAttempt.objects.filter(quiz=quiz, email=email, mobile=mobile)
            if attempt_qs.exists():
                attempt = attempt_qs.latest('date_taken')
                cooldown = datetime.timedelta(hours=COOLDOWN_HOURS)
                now = timezone.now()
                if now - attempt.date_taken < cooldown:
                    remaining = cooldown - (now - attempt.date_taken)
                    remaining_hours = remaining.seconds // 3600
                    remaining_minutes = (remaining.seconds % 3600) // 60
                    user_answers = json.loads(attempt.user_answers) if attempt.user_answers else {}
                    return render(request, 'quiz/quiz_already_taken.html', {
                        'quiz': quiz,
                        'message': "You have already taken this quiz with these details.",
                        'score': attempt.score,
                        'total': quiz.questions.count(),
                        'remaining': f"{remaining_hours} hours and {remaining_minutes} minutes",
                        'user_answers': user_answers,
                    })
        if not email or not mobile:
            return render(request, 'quiz/quiz_start.html', {'quiz': quiz})

    # If email/mobile are in session and quiz not yet taken (or cooldown expired), display quiz questions.
    questions = quiz.questions.all().order_by('order')
    return render(request, 'quiz/quiz_detail.html', {'quiz': quiz, 'questions': questions})

@login_required
def quiz_create_dynamic(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.author = request.user
            quiz.save()
            # Process dynamic questions
            try:
                question_count = int(request.POST.get('question_count', 0))
            except ValueError:
                question_count = 0
            for i in range(question_count):
                q_text = request.POST.get(f'question_text_{i}', '').strip()
                if not q_text:
                    continue
                question = Question.objects.create(quiz=quiz, text=q_text, order=i)
                try:
                    option_count = int(request.POST.get(f'option_count_{i}', 0))
                except ValueError:
                    option_count = 0
                correct_index = request.POST.get(f'correct_option_{i}', None)
                for j in range(option_count):
                    opt_text = request.POST.get(f'option_text_{i}_{j}', '').strip()
                    if not opt_text:
                        continue
                    is_correct = (str(j) == correct_index)
                    Option.objects.create(question=question, text=opt_text, is_correct=is_correct)
            return redirect('quiz_list')
    else:
        form = QuizForm()
    return render(request, 'quiz/quiz_create_dynamic.html', {'form': form})

@login_required
def quiz_edit(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if request.user != quiz.author:
        return HttpResponseForbidden("You are not allowed to edit this quiz.")

    if request.method == 'POST':
        form = QuizForm(request.POST, instance=quiz)
        if form.is_valid():
            quiz = form.save()
            # For simplicity, delete existing questions/options and recreate them
            quiz.questions.all().delete()
            try:
                question_count = int(request.POST.get('question_count', 0))
            except ValueError:
                question_count = 0
            for i in range(question_count):
                q_text = request.POST.get(f'question_text_{i}', '').strip()
                if not q_text:
                    continue
                question = Question.objects.create(quiz=quiz, text=q_text, order=i)
                try:
                    option_count = int(request.POST.get(f'option_count_{i}', 0))
                except ValueError:
                    option_count = 0
                correct_index = request.POST.get(f'correct_option_{i}', None)
                for j in range(option_count):
                    opt_text = request.POST.get(f'option_text_{i}_{j}', '').strip()
                    if not opt_text:
                        continue
                    is_correct = (str(j) == correct_index)
                    Option.objects.create(question=question, text=opt_text, is_correct=is_correct)
            return redirect('quiz_list')
    else:
        form = QuizForm(instance=quiz)

    # Prepare existing quiz data for JavaScript (to pre-populate dynamic fields)
    quiz_data = []
    for question in quiz.questions.all().order_by('order'):
        options = []
        for option in question.options.all():
            options.append({
                'text': option.text,
                'is_correct': option.is_correct,
            })
        quiz_data.append({
            'question_text': question.text,
            'options': options,
        })
    quiz_data_json = json.dumps(quiz_data)

    return render(request, 'quiz/quiz_edit_dynamic.html', {
        'form': form,
        'quiz_data': quiz_data_json,
        'quiz_id': quiz.id
    })

@login_required
def quiz_delete(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if request.user != quiz.author:
        return HttpResponseForbidden("You are not allowed to delete this quiz.")
    if request.method == 'POST':
        quiz.delete()
        return redirect('quiz_list')
    return render(request, 'quiz/quiz_confirm_delete.html', {'quiz': quiz})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'quiz/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'quiz/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')
