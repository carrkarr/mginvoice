from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from oper.models import *
from oper.forms import DepositosForm
from teso.forms import RepartosForm

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
def list_fac_reparto_view(request):
    facturas = Facturas.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(facturas, 20)
    try:
        fac_list = paginator.page(page)
    except PageNotAnInteger:
        fac_list = paginator.page(1)
    except EmptyPage:
        fac_list = paginator.page(paginator.num_pages)

    return render(request, 'teso/list_fac_reparto.html', {'fac_list': fac_list})


def create_reparto(request):
    if request.method == "POST":
        form = RepartosForm(request.POST)  
        if form.is_valid():
            reparto = form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "RepartoListChanged": None,
                        "showMessage": f"{reparto.ID_REPARTO} added."
                    })
                })
    else:
        form = RepartosForm()
    return render(request, 'teso/create_reparto.html', {
        'form': form,
    })


def find_fac(request):
    q = request.GET.get('query')

    if q:
        facturas = Facturas.objects.filter(FOLIO__icontains=q)
    else:
        facturas = Facturas.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(facturas, 30)
    try:
        fac_list = paginator.page(page)
    except PageNotAnInteger:
        fac_list = paginator.page(1)
    except EmptyPage:
        fac_list = paginator.page(paginator.num_pages)

    return render(request, 'teso/list_fac_reparto.html', {'fac_list': fac_list})

def find_fac_f(request):
    q = request.GET.get('query_f')

    if q:
        facturas = Facturas.objects.filter(FECHA_EMISION__icontains=q)
    else:
        facturas = Facturas.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(facturas, 30)
    try:
        fac_list = paginator.page(page)
    except PageNotAnInteger:
        fac_list = paginator.page(1)
    except EmptyPage:
        fac_list = paginator.page(paginator.num_pages)

    return render(request, 'teso/list_fac_reparto.html', {'fac_list': fac_list})

