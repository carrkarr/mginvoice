from django.shortcuts import redirect
from django.shortcuts import render
from .forms import  DepositosForm, EfectivoForm
from .models import *
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import json
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from teso.models import *
class HTTPResponseHXRedirect(HttpResponseRedirect):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self["HX-Redirect"] = self["Location"]
    status_code = 200

# Create your views here.
def create_depo(request):  
    if request.method == "POST":  
        form = DepositosForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/create_depo')
            except:  
                pass 
    else:  
        form = DepositosForm()  
    return render(request,'oper/create_depo.html',{'form':form})

def list_depo_view(request):
    depositos = Depositos.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(depositos, 20)
    try:
        depo_list = paginator.page(page)
    except PageNotAnInteger:
        depo_list = paginator.page(1)
    except EmptyPage:
        depo_list = paginator.page(paginator.num_pages)

    return render(request, 'oper/list_depo.html', {'depo_list': depo_list})


@require_http_methods(['DELETE'])
def delete_depo(request, id):
    Depositos.objects.filter(ID_DEPOSITO=id).delete()
    depositos = Depositos.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(depositos, 20)
    try:
        depo_list = paginator.page(page)
    except PageNotAnInteger:
        depo_list = paginator.page(1)
    except EmptyPage:
        depo_list = paginator.page(paginator.num_pages)

    return render(request, 'oper/table_depo.html', {'depo_list': depo_list})

#***********************************
#***********************************

def find_depo(request):
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

    return render(request, 'oper/list_depo.html', {'depo_list': depo_list})

def find_depo_f(request):
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

    return render(request, 'oper/list_depo.html', {'depo_list': depo_list})

#*********************************
#*********************************
from django.urls import reverse_lazy
def create_efe(request):
    if request.method == "POST":
        form = EfectivoForm(request.POST)
        if form.is_valid():
            efe = form.save()
		# Creamos el registro de Caja ID_DEPOSITO      = Depositos.objects.get(ID_DEPOSITO = 0),
            obj, get_or_create = Caja.objects.filter(ID_EFECTIVO=efe.ID_EFECTIVO).get_or_create(ID_DEPOSITO      = None,
                                                ID_EFECTIVO      = Efectivo.objects.get(ID_EFECTIVO = efe.ID_EFECTIVO),
                                                IMPORTE          = efe.IMPORTE_DISP,
                                                IMPORTE_DISP     = efe.IMPORTE_DISP,
                                                ID_MONEDA        = Monedas.objects.get(ID_MONEDA = 1) ,
                                                )
            #obj.save()

            return HTTPResponseHXRedirect(redirect_to=reverse_lazy("list-efe"))

            '''
            
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "depoListChanged": None,
                        "showMessage": f"{efe.ID_EFECTIVO} added."
                    })
                })
                '''
    else:
        form = EfectivoForm()
    return render(request, 'oper/create_efe.html', {
        'form': form,
    })


def list_efe_view(request):
    efectivo = Efectivo.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(efectivo, 20)
    try:
        efe_list = paginator.page(page)
    except PageNotAnInteger:
        efe_list = paginator.page(1)
    except EmptyPage:
        efe_list = paginator.page(paginator.num_pages)

    return render(request, 'oper/list_efe.html', {'efe_list': efe_list})

def find_efe(request):
    q = request.GET.get('query')

    if q:
        efectivo = Efectivo.objects.filter(ID_EFECTIVO__icontains=q)
    else:
        efectivo = Efectivo.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(efectivo, 20)
    try:
        efe_list = paginator.page(page)
    except PageNotAnInteger:
        efe_list = paginator.page(1)
    except EmptyPage:
        efe_list = paginator.page(paginator.num_pages)

    return render(request, 'oper/list_efe.html', {'efe_list': efe_list})


def find_efe_f(request):
    q = request.GET.get('query_f')

    if q:
        efectivo = Efectivo.objects.filter(FECHA_DEPOSITO__icontains=q)
    else:
        efectivo = Efectivo.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(efectivo, 20)
    try:
        efe_list = paginator.page(page)
    except PageNotAnInteger:
        efe_list = paginator.page(1)
    except EmptyPage:
        efe_list = paginator.page(paginator.num_pages)

    return render(request, 'oper/list_efe.html', {'efe_list': efe_list})


@require_http_methods(['DELETE'])
def delete_efe(request, id):
    Efectivo.objects.filter(ID_EFECTIVO=id).delete()
    efectivo = Efectivo.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(efectivo, 20)
    try:
        efe_list = paginator.page(page)
    except PageNotAnInteger:
        efe_list = paginator.page(1)
    except EmptyPage:
        efe_list = paginator.page(paginator.num_pages)

    return render(request, 'oper/table_efe.html', {'efe_list': efe_list})