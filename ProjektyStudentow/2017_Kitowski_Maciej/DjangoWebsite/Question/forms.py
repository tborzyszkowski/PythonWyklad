from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from Question import models

class NewQuestion(forms.ModelForm):
    author = forms.CharField(
        label = "Author",
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'author'}),
        required = False
    )
    title = forms.CharField(
        label = "Title",
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'title', 'placeholder': 'Title'})
    )
    content = forms.CharField(
        label = "Content",
        widget=forms.Textarea(attrs={'class': 'form-control', 'name': 'content', 'placeholder': 'Question...'})
    )
    categories = forms.ModelMultipleChoiceField(
        label = "Categories",
        widget=forms.SelectMultiple(attrs={'class': 'form-control', 'name': 'categories'}),
        queryset=models.Category.objects.all()
    )

    class Meta:
        model = models.Question
        fields = ('title', 'content', 'categories')

class EditAnswer(forms.ModelForm):
    author = forms.CharField(
        label = "Author",
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'author'}),
        required = False
    )
    content = forms.CharField(
        label = "Content",
        widget=forms.Textarea(attrs={'class': 'form-control', 'name': 'content', 'rows':'2'})
    )

    class Meta:
        model = models.Answer
        fields = ('content',)

class Login(AuthenticationForm):
    username = forms.CharField(
        label = "Username",
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        label = "Username",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password', 'placeholder': 'Password'})
    )

class Register(UserCreationForm):
    username = forms.CharField(
        label = "Username",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Username', 'name': 'username'})
    )
    email = forms.CharField(
        label = "E-mail",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'E-mail', 'name': 'email'})
    )
    password1 = forms.CharField(
        label = "Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password', 'name': 'password1'})
    )
    password2 = forms.CharField(
        label = "Repeat password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Repeat password', 'name': 'password2'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
