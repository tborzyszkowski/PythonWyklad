import datetime

from django.db import models
from django.utils import timezone

"""class Test(models.Model):
    test_name = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.test_name
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)"""

class GraphType(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    def __str__(self):
        return self.name

class Graphs(models.Model):
    matrix = models.CharField(max_length=200)
    add_date = models.DateTimeField('date added')
    graph_type = models.ForeignKey(GraphType, on_delete=models.CASCADE)
    editCounter = models.IntegerField(default=0)
    wrongCounter = models.IntegerField(default=0)
    def __str__(self):
        return self.matrix
    """@classmethod
    def create(cls, matrix):
        Graphs = cls(matrix=matrix)
        # do something with the book
        return Graphs"""
    def was_published_recently(self):
        return self.add_date >= timezone.now() - datetime.timedelta(days=1)
