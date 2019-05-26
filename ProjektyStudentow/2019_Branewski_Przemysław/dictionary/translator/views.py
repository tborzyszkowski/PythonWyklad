from django.shortcuts import render, get_object_or_404

# Create your views here.


from .models import Question


def index(request):
    question_list = Question.objects.all()
    context = {'question_list': question_list}
    return render(request, 'translator/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'translator/detail.html', {'question': question})