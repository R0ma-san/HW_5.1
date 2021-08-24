from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponseNotFound
from .models import Question
from .forms import QuestionsForm

def questions(request):

    questions = Question.objects.all()
    return render(request, 'questions/questions.html', {'questions': questions})

def new_questions(request):
    
    if request.method == "POST":
        form = QuestionsForm(request.POST)
        if form.is_valid():
            questions = form.save(commit=False)
            questions.save()
            return redirect('news')
    else:
        form = QuestionsForm()
    return render(request, 'questions/new_question.html', {'form': form})


def questions_detail(request, pk):
    questions_detail = get_object_or_404(Question, pk=pk)
    return render(request, 'questions/questions_detail.html', {'questions_detail': questions_detail})

def questions_delete(request, pk):
    
    try:
        questions = Question.objects.get(id=pk)
        questions.delete()
        return redirect('questions')
    except questions.DoesNotExist:
        return HttpResponseNotFound("<h2>Вопрос не найден</h2>")