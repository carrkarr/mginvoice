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
    print ('111')
    if request.method == "POST":
        form = DepositosForm(request.POST)  
        if form.is_valid():
            movie = form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "depoListChanged": None,
                        "showMessage": f"{Depositos.CVE_FOLIO} added."
                    })
                })
    else:
        form = DepositosForm()
    print ('22')
    return render(request, 'deposito_form.html', {
        'form': form,
    })
