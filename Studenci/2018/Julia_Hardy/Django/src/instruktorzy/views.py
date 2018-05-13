from django.views.generic import ListView
from django.shortcuts import render

# Create your views here.

from .models import Instruktor


class InstruktorListView(ListView):
    queryset = Instruktor.objects.all()
    template_name = "instruktorzy/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(InstruktorListView, self).get_context_data(*args, **kwargs)
        print(context)
        return context



def instruktor_list_view(request):
    queryset = Instruktor.objects.all()
    context = {
        'object_list': queryset,
    }
    return render(request, "instruktorzy/list.html", context)