from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect

from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core import serializers
from django.conf import settings

import os

from .models import Product

class IndexView(generic.ListView):
	template_name = 'mmapp/home.html'
	context_object_name = 'latest_product_list'

	def get_queryset(self):
		return Product.objects.order_by('-date')

class crud():
	def savedata(request):
		# model = Product
		# template_name = 'mmapp/results.html'
		sd = Product(name=request.POST['name'], items=request.POST['items'], date=timezone.now(), image=request.FILES['image'], shop=request.POST['shop'],checked='0')
		sd.save()
		# return redirect()

		return HttpResponseRedirect(reverse('mmapp:index'))

	def editdata(request, data_id):
		# data = Product.objects.get(id=data_id)
		# return HttpResponse(dt)
		ed = get_object_or_404(Product, pk=data_id)
		# return HttpResponse(data)
		alldata = Product.objects.order_by('-date') #serializers.deserialize('json', Product.objects.all())
		return render(request, 'mmapp/home.html', {'data': ed, 'qid' : data_id, 'getdata' : alldata})

	def updatedata(request):
		ud = Product.objects.get(id=request.POST['qid'])
		
		imagePath = os.path.join(settings.MEDIA_ROOT, ud.image.name)

		if 'image' in request.FILES:
			ud.image = request.FILES['image']
			if os.path.isfile(imagePath):
				os.remove(imagePath)


		ud.name=request.POST['name']
		ud.items=request.POST['items']
		ud.shop=request.POST['shop']
		ud.save()

		return HttpResponseRedirect(reverse('mmapp:index'))

	def deletedata(request, data_id):
		dd = Product.objects.get(id=data_id)

		imagePath = os.path.join(settings.MEDIA_ROOT, dd.image.name)

		if os.path.isfile(imagePath):
			os.remove(imagePath)

		dd.delete()

		return HttpResponseRedirect(reverse('mmapp:index'))
