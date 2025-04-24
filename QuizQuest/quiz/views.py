# quiz/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseForbidden, HttpResponse
from django.contrib.auth.decorators import user_passes_test, login_required
from django.utils import timezone
from .models import Quiz, Question, Option, Score, TestAttempt, EmailOTP
from .forms import QuizForm, SignUpForm, QuestionForm, EmailForm, OTPForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
import json
import datetime
from django.core.mail import send_mail
import random
from django.db.models import Avg, Count
from django.forms.models import model_to_dict

# Set the cooldown period (in hours) for retaking the quiz
COOLDOWN_HOURS = 24  # Change to 168 for one week, etc.

def home(request):
    return render(request, 'quiz/home.html')

def superuser_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)



def quiz_list(request):
    quizzes = Quiz.objects.annotate(
        total_attempts=Count('attempts'),
        avg_score=Avg('attempts__score')
    )

    user_attempts = {}
    if request.user.is_authenticated and not request.user.is_superuser:
        for quiz in quizzes:
            attempt = TestAttempt.objects.filter(quiz=quiz, email=request.user.email).order_by('-date_taken').first()
            user_attempts[quiz.id] = attempt

    return render(request, 'quiz/quiz_list.html', {
        'quizzes': quizzes,
        'user_attempts': user_attempts,
    })


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

@superuser_required
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

@superuser_required
def quiz_edit(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    form = QuizForm(request.POST or None, instance=quiz)

    if request.method == 'POST' and form.is_valid():
        form.save()

        # Delete existing questions and options before re-saving
        quiz.questions.all().delete()

        # Handle dynamic questions and options
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
                is_correct = str(j) == str(correct_index)
                Option.objects.create(question=question, text=opt_text, is_correct=is_correct)

        return redirect('quiz_list')  # redirects to /quizzes/

    # For GET: prepare quiz_data for JS to load into form
    questions_data = []
    for question in quiz.questions.all().order_by('order'):
        options = list(question.options.values('text', 'is_correct'))
        questions_data.append({
            'text': question.text,
            'order': question.order,
            'options': options
        })

    quiz_data = json.dumps(questions_data)

    return render(request, 'quiz/quiz_edit_dynamic.html', {
        'form': form,
        'quiz': quiz,
        'quiz_data': quiz_data
    })

@superuser_required
def quiz_delete(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if request.user != quiz.author:
        return HttpResponseForbidden("You are not allowed to delete this quiz.")
    if request.method == 'POST':
        quiz.delete()
        return redirect('quiz_list')
    return render(request, 'quiz/quiz_confirm_delete.html', {'quiz': quiz})

@superuser_required
def view_results(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    results = TestAttempt.objects.filter(quiz=quiz)
    return render(request, 'quiz/view_results.html', {'quiz': quiz, 'results': results})

# @login_required
def send_otp(request, quiz_id):
    if request.user.is_superuser:
        return HttpResponse("Superusers are not allowed to take quizzes.")

    quiz = get_object_or_404(Quiz, pk=quiz_id)

    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            otp = str(random.randint(100000, 999999))
            EmailOTP.objects.create(email=email, otp=otp)
            send_mail(
                "QuizQuest OTP Verification",
                f"Your OTP is: {otp}",
                "noreply@quizquest.com",
                [email]
            )
            request.session['quiz_email'] = email
            return redirect('verify_otp', quiz_id=quiz_id)
    else:
        form = EmailForm()
    return render(request, 'quiz/send_otp.html', {'form': form, 'quiz': quiz})

# @login_required
def verify_otp(request, quiz_id):
    email = request.session.get('quiz_email')
    if not email:
        return redirect('send_otp', quiz_id=quiz_id)

    if request.method == "POST":
        form = OTPForm(request.POST)
        if form.is_valid():
            entered_otp = form.cleaned_data['otp']
            if EmailOTP.objects.filter(email=email, otp=entered_otp).exists():
                request.session['otp_verified'] = True
                return redirect('take_quiz', quiz_id=quiz_id)
    else:
        form = OTPForm()
    return render(request, 'quiz/verify_otp.html', {'form': form})


@user_passes_test(lambda u: not u.is_superuser)
def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)

    # Check OTP session
    if not request.session.get('otp_verified'):
        return redirect('send_otp', quiz_id=quiz_id)

    email = request.session.get('quiz_email')
    if not email:
        return redirect('send_otp', quiz_id=quiz_id)

    # 🔁 POST = User submitted quiz
    if request.method == "POST":
        questions = quiz.questions.all()
        score = 0
        total = questions.count()
        user_answers = {}

        for question in questions:
            selected_option_id = request.POST.get(f"question_{question.id}")
            if selected_option_id:
                selected_option = get_object_or_404(Option, pk=selected_option_id)
                user_answers[str(question.id)] = selected_option.id
                if selected_option.is_correct:
                    score += 1

        # Save attempt
        TestAttempt.objects.create(
            quiz=quiz,
            email=email,
            mobile="Anonymous",  # Optional
            score=score,
            user_answers=json.dumps(user_answers)
        )

        return render(request, 'quiz/quiz_result.html', {
            'quiz': quiz,
            'score': score,
            'total': total,
        })

    # 🔎 GET = Check if quiz was already taken
    attempt_qs = TestAttempt.objects.filter(quiz=quiz, email=email)
    if attempt_qs.exists():
        attempt = attempt_qs.latest('date_taken')
        cooldown = datetime.timedelta(hours=COOLDOWN_HOURS)
        now = timezone.now()

        if now - attempt.date_taken < cooldown:
            remaining = cooldown - (now - attempt.date_taken)
            remaining_hours = remaining.seconds // 3600
            remaining_minutes = (remaining.seconds % 3600) // 60

            user_answers_raw = attempt.user_answers
            print(f'user_answers_raw:', user_answers_raw)
            try:
                user_answers = json.loads(user_answers_raw)
                print(f'user_answers:', user_answers)
            except:
                user_answers = {}

            for question in quiz.questions.all():
                str_qid = str(question.id)
                selected_option_id = user_answers.get(str_qid)
                print(f'selected_option_id: ', selected_option_id, f'question.id: ', question.id)
                try:
                    question.selected_option_id = int(selected_option_id)
                    print(f'question.selected_option_id: ', question.selected_option_id)
                except (TypeError, ValueError):
                    question.selected_option_id = None

            print(f'question.selected_option_id: ', question.selected_option_id)
            print(f'quiz: ', quiz, f'score:', attempt.score, 'total:', quiz.questions.count(), 'user_answers:', user_answers)
            return render(request, 'quiz/quiz_already_taken.html', {
                'quiz': quiz,
                'message': "You have already taken this quiz with these details.",
                'score': attempt.score,
                'total': quiz.questions.count(),
                'remaining': f"{remaining_hours} hours and {remaining_minutes} minutes",
                'user_answers': user_answers,
            })

    # 📄 Show quiz questions (first-time or after cooldown)
    questions = quiz.questions.all()
    return render(request, 'quiz/take_quiz.html', {
        'quiz': quiz,
        'questions': questions
    })


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
