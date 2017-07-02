from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
import markdown
import logging

from django.utils.decorators import method_decorator

from catalog.forms import BlogArticleForm, BlogCommentForm
from .models import Article as ArticleModel
from .models import Comment as CommentModel
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.


logger = logging.getLogger(__name__)

@method_decorator(login_required(login_url="login", redirect_field_name=None), name='dispatch')
class IndexView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        article_list = ArticleModel.objects.filter(status='p')
        return article_list

@login_required()
def AddArticleView(request):
    form = BlogArticleForm()
    if request.method == 'POST':
        form = BlogArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            author = request.user
            new_record = ArticleModel(title = title, body = body, author = author, status = 'p')
            new_record.save()

            return redirect('catalog:index')
    return render(request, 'blog/add_article.html', {'form': form})

@method_decorator(login_required(login_url="login", redirect_field_name=None), name='dispatch')
class ArticleDetailView(DetailView):
    template_name = 'blog/article_detail.html'
    model = ArticleModel
    context_object_name = "article_detail"
    pk_url_kwarg = 'article_id'
    def get_object(self, queryset=None):
        article = super(ArticleDetailView, self).get_object()
        article.body = markdown.markdown(article.body, safe_mode='escape',
        extensions=[
            'markdown.extensions.nl2br',
            'markdown.extensions.fenced_code'
        ])
        return article

    def get_context_data(self, **kwargs):
        kwargs['comment_list'] = self.object.comment_set.all()
        kwargs['form'] = BlogCommentForm()
        kwargs['article'] = self.get_object(self)
        kwargs['article_id'] = self.get_object(self).get_article_id
        return super(ArticleDetailView, self).get_context_data(**kwargs)


@login_required()
def CommentView(request, article_id):
    def get_queryset(self):
        article = get_object_or_404(ArticleModel, pk=article_id)
        comment_list = CommentModel.objects.filter(article=article)
        return comment_list

    form = BlogCommentForm()
    if request.method == 'POST':
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            author = request.user
            body = form.cleaned_data['body']
            article = get_object_or_404(ArticleModel, pk=article_id)
            new_record = CommentModel(user_name=author,
                                 body=body,
                                article=article)
            new_record.save()
            return redirect('catalog:article_detail', article_id=article_id)
    return render(request, 'blog/comment.html', {'form': form})

@login_required()
def LikeView(request, article_id):
    if request.method == 'POST':
        article = get_object_or_404(ArticleModel, pk=article_id)
        article.likes += 1
        article.save()
        return redirect('catalog:article_detail', article_id=article_id)

@login_required()
def DislikeView(request, article_id):
    if request.method == 'POST':
        article = get_object_or_404(ArticleModel, pk=article_id)
        article.dislikes += 1
        article.save()
        return redirect('catalog:article_detail', article_id=article_id)

def RegisterAccountView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required()
def CommentRemoveView(request, article_id, comment_id):
    if request.method == 'POST':
        comment = get_object_or_404(CommentModel, pk=comment_id)
        comment.delete(keep_parents=True)
    return redirect('catalog:article_detail', article_id=article_id)

def LogOutView(request):
    logout(request)
    return redirect('login')