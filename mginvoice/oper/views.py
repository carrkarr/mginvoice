from django.shortcuts import render
from django.shortcuts import redirect
from .forms import  DepositoForm
from .models import *
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# Create your views here.
def create_depo(request):  
    if request.method == "POST":  
        form = DepositoForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/create_depo')  
            except:  
                pass 
    else:  
        form = DepositoForm()  
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
