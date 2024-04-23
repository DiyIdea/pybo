from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse (삭제 2-04에서)
from django.shortcuts import render, get_object_or_404, redirect # 2-04 "404페이지 추가,
from django.utils import timezone
from .models import Question, Answer
from .forms import QuestionForm


def index(request) : #url.py 에서 path('',view.index)로 참조중.
   #return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")(삭제 2-04에서)
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list' : question_list}
    return render(request, 'pybo/question_list.html', context)# qustion_list.html로

def detail(request, question_id): #url.py 에서 path('<int:question_id>/',view.detail)로 참조중.
    question = get_object_or_404(Question, pk=question_id) #Question.objects.get(id=question_id) #2-04 페이지추가 및 삭제
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    answer.save()
    #question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail', question_id=question.id)

def question_create(request):
    form = QuestionForm()
    return render(request, 'pybo/question_form.html', {'form': form})