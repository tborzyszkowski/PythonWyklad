import Question.forms as fr
from Question import models as md
from django.db.models import Count, Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models.functions import Coalesce
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, DeleteView, UpdateView

class Index(ListView):
    template_name = 'main/index.html'
    context_object_name = 'questions'
    model = md.Question
    paginate_by = 13

    def get_queryset(self):
        sortbyColumn = {'date-asc':'askDate', 'date-desc':'-askDate', 'votes-asc':'votesSum', 'votes-desc':'-votesSum', 'views-asc':'viewsCount', 'views-desc':'-viewsCount', 'answers-asc':'answersCount', 'answers-desc':'-answersCount' }
        qr = super(Index, self).get_queryset()

        if 'category' in self.kwargs:
            qr = qr.filter(categories__name__iexact = self.kwargs['category'])

        if 'sortby' in self.kwargs and self.kwargs['sortby'] in sortbyColumn:
            if self.kwargs['sortby'] == 'votes-asc' or self.kwargs['sortby'] == 'votes-desc':
                qr = qr.annotate(votesSum=Coalesce(Sum('votes__vote'), 0)).order_by(sortbyColumn[self.kwargs['sortby']])
            elif self.kwargs['sortby'] == 'views-asc' or self.kwargs['sortby'] == 'views-desc':
                qr = qr.annotate(viewsCount=Count('views', distinct=True)).order_by(sortbyColumn[self.kwargs['sortby']])
            elif self.kwargs['sortby'] == 'answers-asc' or self.kwargs['sortby'] == 'answers-desc':
                qr = qr.annotate(answersCount=Count('views', distinct=True)).order_by(sortbyColumn[self.kwargs['sortby']])
            else:
                qr = qr.order_by(sortbyColumn[self.kwargs['sortby']])
        else:
            qr = qr.order_by(sortbyColumn['date-desc'])

        return qr

class Categories(ListView):
    template_name = 'main/categories.html'
    context_object_name = 'categories'
    model = md.Category
    paginate_by = 21

class Question(DetailView):
    template_name = 'main/question.html'
    model = md.Question

    def getIP(self):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request, *args, **kwargs):
        if 'answerVote' in request.POST:
            agent = self.request.META.get('HTTP_USER_AGENT')
            vot = md.Vote(user = request.user, useragent = agent, ip = self.getIP(), vote = request.POST['answerVote'])
            if md.Answer.objects.get(pk=request.POST['pk']).isAuthorVote(vot) == False:
                md.Answer.objects.get(pk=request.POST['pk']).saveOrUpdateVote(vot)

        if 'questionVote' in request.POST:
            agent = self.request.META.get('HTTP_USER_AGENT')
            vot = md.Vote(user = request.user, useragent = agent, ip = self.getIP(), vote = request.POST['questionVote'])
            if md.Question.objects.get(pk=self.kwargs['pk']).isAuthorVote(vot) == False:
                md.Question.objects.get(pk=self.kwargs['pk']).saveOrUpdateVote(vot)

        if 'answer' in request.POST:
            ans = md.Answer.objects.create(author=request.user, content = request.POST['answer'])
            md.Question.objects.get(pk=self.kwargs['pk']).answers.add(ans)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
    def get_context_data(self, **kwargs):
        agent = self.request.META.get('HTTP_USER_AGENT')
        if self.request.user.is_authenticated():
            view = md.View.objects.create(user = self.request.user, useragent = agent, ip = self.getIP() )
        else:
            view = md.View.objects.create(useragent = agent, ip = self.getIP() )
        md.Question.objects.get(pk=self.kwargs['pk']).views.add(view)

        context = super(Question, self).get_context_data(**kwargs)
        return context

class NewQuestion(FormView):
    template_name = 'main/newQuestion.html'
    form_class = fr.NewQuestion
    success_url = '/'
    
    def form_valid(self, form):
        candidate = form.save(commit=False)
        candidate.author = self.request.user
        candidate.save()
        form.save_m2m()
        return super(NewQuestion, self).form_valid(candidate)

class EditQuestion(UpdateView):
    template_name = "modify/edit_question.html"
    form_class = fr.NewQuestion
    model = md.Question
    success_url = '/'

class DeleteQuestion(DeleteView):
    template_name = 'modify/delete_question.html'
    model = md.Question
    success_url = '/'

    def post(self, request, *args, **kwargs):
        print request.POST
        if 'cancel' in request.POST:
            return redirect('question', pk=kwargs['pk'])
        else:
            self.get_object().views.all().delete()
            self.get_object().votes.all().delete()

            for answ in self.get_object().answers.all():
                answ.votes.all().delete()

            self.get_object().answers.all().delete()
            return super(DeleteQuestion, self).post(request, *args, **kwargs)

class EditAnswer(UpdateView):
    template_name = 'modify/edit_answer.html'
    form_class = fr.EditAnswer
    success_url = '/'
    model = md.Answer

    def form_valid(self, form):
        form.save()
        question = self.get_object().question_set.all()[0]
        return redirect('question', pk=question.pk)

    def get_context_data(self, **kwargs):
        context = super(EditAnswer, self).get_context_data(**kwargs)
        question = self.get_object().question_set.all()[0]
        context['question'] = question

        return context

class DeleteAnswer(DeleteView):
    template_name = 'modify/delete_answer.html'
    model = md.Answer
    success_url = '/'

    def post(self, request, *args, **kwargs):
        print request.POST
        if 'cancel' in request.POST:
            question = self.get_object().question_set.all()[0]
            return redirect('question', pk=question.pk)
        else:
            self.get_object().votes.all().delete()
            return super(DeleteAnswer, self).post(request, *args, **kwargs)

class Register(FormView):
    template_name = 'auth/register.html'
    form_class = fr.Register
    success_url = '/'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return super(Register, self).form_valid(form)
