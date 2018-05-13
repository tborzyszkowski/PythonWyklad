from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Zapisy
from .forms import ZapisyForm

# Create your views here.


def zapisy_create(request):
    form = ZapisyForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        instance.user = request.user
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(reverse('zapisy'))
    context = {
        "form": form,

    }
    return render(request, "zapisy/form.html", context)

def zapisy_detail(request, id=None):
    instance = get_object_or_404(Zapisy, id=id)
    context = {
        "instance": instance,
    }
    return render(request, "zapisy/detail.html", context)


def zapisy_list(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('logowanie'))
    queryset_list = Zapisy.objects.filter(user=request.user)
    context = {
            "object_list": queryset_list,
         }

    return render(request, "zapisy/list.html", context)


def zapisy_update(request, id=None):
    instance = get_object_or_404(Zapisy, id=id)
    form = ZapisyForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
        messages.success(request, "Item Saved")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, "zapisy/form.html", context)


def zapisy_delete(request, id=None):
    instance = get_object_or_404(Zapisy, id=id)
    instance.delete()
    messages.success(request, "Successfully Deleted")
    return HttpResponseRedirect(reverse('zapisy'))
    context = {
        "title": "Delete"
    }
    return render(request, "list.html", context)
