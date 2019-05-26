from django.shortcuts import get_object_or_404, render
import datetime
from django.utils import timezone

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.http import Http404
from django.template import loader
from django.utils.datastructures import MultiValueDictKeyError

from .models import GraphType,Graphs
import GraphMaster.Graph
from GraphMaster.Graph import *

def input(request):
    string="""0 1 0 0 0 
    0 0 1 0 0 
    0 0 0 1 0 
    1 0 0 0 1 
    0 1 0 0 0 """
    testGraph=Graph(string)
    context = {'vertexsPosition': testGraph.getGraphicPosition(300)[0], 'edgesPosition': testGraph.getGraphicPosition(300)[1]}
    return render(request, 'GraphMaster/input.html', context)

def answer(request, graph_id):

    g = get_object_or_404(Graphs, pk=graph_id)
    try:
        action=request.POST['action']
        matrixAsString=request.POST['matrix']
    except MultiValueDictKeyError:
        matrixAsString="0 1\n1 0"
        action='Edytuj'
    g.editCounter=g.editCounter+1
    g.matrix=matrixAsString
    try:
        testGraph=Graph(matrixAsString)
    except IncorrectMatrix:
        gType = GraphType.objects.get(name="Inny")
        g.save()
        g.wrongCounter=g.wrongCounter+1
        context = {'graph': g, 'matrixIncorrect':1}
        return render(request, 'GraphMaster/answer.html', context)
    if(action=="Edytuj"):
        gType = GraphType.objects.get(name="Ścieżka" if testGraph.isPathGraph() else ("Pełny" if testGraph.isCompleteGraph() else ("Cykl" if testGraph.isCycleGraph() else ("Drzewo" if testGraph.isTree() else "Inny"))))
        g.graph_type = gType
        g.save()
        context = {'graph': g,'vertexsPosition': testGraph.getGraphicPosition(600)[0], 'edgesPosition': testGraph.getGraphicPosition(600)[1],
                   'edgeCount': testGraph.edgeCount(), 'vertexCount':testGraph.vertexCount(), 'degrees': testGraph.getDegrees(), 'type':gType.name,
                   'description': g.graph_type.description}
        return render(request, 'GraphMaster/answer.html', context)
    elif(action=="Usun"):
        g.delete()
        g=Graphs(matrix="0 1\n1 0", add_date=timezone.now(), graph_type=GraphType.objects.get(name="Pełny"))
        g.save()
        context = {'graph': g}
        return render(request, 'GraphMaster/index.html', context)


def index(request):
    g=Graphs(matrix="0 1\n1 0", add_date=timezone.now(), graph_type=GraphType.objects.get(name="Pełny"))
    g.save()
    context = {'graph': g}
    return render(request, 'GraphMaster/index.html', context)
