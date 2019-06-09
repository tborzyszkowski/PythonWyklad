from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Translation(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    translation_text = models.CharField(max_length=50)

    def __str__(self):
        return self.translation_text