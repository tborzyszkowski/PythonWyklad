from django import forms
from .models import Article, Comment

class BlogArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body']
        widgets = {
            'title' : forms.Textarea(attrs={
                'placeholder' : 'title',
                'class' : 'form-control',
                'rows' : 1,
                'cols' : 80,
        }),
            'body' : forms.Textarea(attrs={
                'placeholder' : 'body',
                'class' : 'form-control',
                'rows' : 10,
                'cols' : 80,
            })
        }


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'placeholder': 'body',
                                          'class': 'form-control',
                                          'rows': 4,
                                          }),
        }