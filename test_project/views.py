import pytz
from django.views.generic.dates import YearArchiveView

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from . import models
from django.utils import timezone
from .models import *
def index(request):
	model= UserProfile
	latest_cromos_list=Cromo.objects.order_by('-pub_date')
	template=loader.get_template('test_project/album/PaginaPrincipal.html')
	server_time=timezone.now
	
	context={
		'latest_cromos_list':latest_cromos_list,
		'UserProfile':UserProfile,
		'server_time':server_time,

	}
	return HttpResponse(template.render(context,request))
	
def album(request):
	list_pagina=Pagina.objects.order_by('-id').reverse()
	template=loader.get_template('test_project/album/pagina_principal.html')
	context={
		'list_pagina':list_pagina,
	}
	return HttpResponse(template.render(context,request))

def detail(request, cromo_id):
    cromo = get_object_or_404(Cromo, pk=cromo_id)
    return render(request, 'test_project/detail.html', {'cromo': cromo})

def pagina(request,pagina_id):
	pagina= get_object_or_404(Pagina,pk=pagina_id)
	list_cromo=Cromo.objects.order_by('-id').reverse()
	context={
		'list_cromo':list_cromo,
		'pagina':pagina,
	}
	return render(request,'test_project/album/pagina.html',context)
