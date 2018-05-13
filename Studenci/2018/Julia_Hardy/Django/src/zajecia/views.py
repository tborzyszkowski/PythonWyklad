from django.shortcuts import render
from django.views.generic import ListView
from .models import Zajecia
from django.views.generic import DetailView, ListView
from django.shortcuts import render, get_object_or_404
# Create your views here.


class ZajeciaListView(ListView):
    queryset = Zajecia.objects.all()
    template_name = "zajecia/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ZajeciaListView, self).get_context_data(*args, **kwargs)
        print(context)
        return context



def zajecia_list_view(request):
    queryset = Zajecia.objects.all()
    context = {
        'object_list': queryset,
    }
    return render(request, "zajecia/list.html", context)

