from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from oper.models import *
from oper.forms import DepositosForm

from django.contrib import messages #import messages
# Create your views here.

import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

def list_depo_up_view(request):
    depositos = Depositos.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(depositos, 20)
    try:
        depo_list = paginator.page(page)
    except PageNotAnInteger:
        depo_list = paginator.page(1)
    except EmptyPage:
        depo_list = paginator.page(paginator.num_pages)

    return render(request, 'teso/list_depo_up.html', {'depo_list': depo_list})

def create_depo(request):
    if request.method == "POST":
        form = DepositosForm(request.POST)  
        if form.is_valid():
            depo = form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "depoListChanged": None,
                        "showMessage": f"{depo.CVE_FOLIO} added."
                    })
                })
    else:
        form = DepositosForm()
    return render(request, 'create_depo.html', {
        'form': form,
    })

def edit_depo(request, pk):
    depo = get_object_or_404(Depositos, ID_DEPOSITO=pk)
    if request.method == "POST":
        form = DepositosForm(request.POST, instance=depo)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "depoListChanged": None,
                        "showMessage": f"{depo.CVE_FOLIO} Actualizado."
                    })
                }
            )
    else:
        form = DepositosForm(instance=depo)
    return render(request, 'teso/update_depo.html', {
        'form': form,
        'depo': depo,
    })


#***********************************
#***********************************

def find_depo_up(request):
    q = request.GET.get('query')

    if q:
        depositos = Depositos.objects.filter(CVE_FOLIO__icontains=q)
    else:
        depositos = Depositos.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(depositos, 20)
    try:
        depo_list = paginator.page(page)
    except PageNotAnInteger:
        depo_list = paginator.page(1)
    except EmptyPage:
        depo_list = paginator.page(paginator.num_pages)

    return render(request, 'teso/list_depo_up.html', {'depo_list': depo_list})

def find_depo_f_up(request):
    q = request.GET.get('query_f')

    if q:
        depositos = Depositos.objects.filter(FECHA_DEPOSITO__icontains=q)
    else:
        depositos = Depositos.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(depositos, 20)
    try:
        depo_list = paginator.page(page)
    except PageNotAnInteger:
        depo_list = paginator.page(1)
    except EmptyPage:
        depo_list = paginator.page(paginator.num_pages)

    return render(request, 'teso/list_depo_up.html', {'depo_list': depo_list})

#*********************************
#*********************************


def modal(request):
    print ('MODALL')
    form = DepositosForm()
    if request.method == 'POST':
        print ('IFFFF')
        form=DepositosForm(request.POST)
        if form.is_valid():
            form.save()
            html = "<div id='email-error' _='on load wait 1s trigger closeModal'>Success</div>"
            return HttpResponse(html, headers={'HX-Trigger': 'newList'})
        return HttpResponse('no')
    print ('CONTINUA MODALL')
    return render(request, 'teso/modal.html', {'form':form})
