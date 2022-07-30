from ast import Not
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import redirect
from django.template import RequestContext
from django.shortcuts import render
from django.views.generic import ListView
from fac.forms import CargaFacForm, FacturaForm
import datetime as dt

import pandas as pd
import re
from django.db.models import Q
from .models import *
from django.utils.dateparse import parse_datetime
from datetime import datetime
from django.utils.formats import get_format

from django.contrib import messages #import messages
from django.core.exceptions import ValidationError
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.generic.base import View

from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required()
def upload_fac(request):
    try:
        if request.method == 'POST' and request.FILES['myfile']:

            form = CargaFacForm(request.POST)

            return render(request, 'fac/archexcel.html',{'form': form})
    except Exception as identifier:
        print(identifier)
        form = CargaFacForm()

    form = CargaFacForm()
    return render(request, 'fac/archexcel.html',{'form': form})

@login_required()
def act_load_fac(request):
    try:
        if request.method == 'POST':

            form = CargaFacForm(request.POST)
            vusername = request.user
              # Obtengo el usuario de la sesion y lo asigno a la variable para ser salvado.

            # Esta funciona y valida que se teclee algo en la pantalla
            myfile = request.FILES.get("docfile", "Guest")

            try:

                #empexceldata = pd.read_csv(myfile, encoding='utf-8')
                empexceldata = pd.read_excel(myfile)

            except Exception as identifier:
                messages.error(request, 'Hay caracteres raros, verificar su archivo... ')
                return render(request, 'fac/archexcel.html',{'form': form})

            dbframe = empexceldata
            #print (dbframe)
            #Leo el encabezado
            # ['NOMBRE RECEPTOR', 'RFC', 'Folio', 'NOMBRE DE EMISOR', 'RFC EMISOR', 'TIPO DE DOCUMENTO', 'FECHA DE EMISION', 'MONEDA', 'ESTADO', ' SUBTOTAL ', ' TOTAL ', ' IVA ', 'AFILIADO']
            list_header = dbframe.columns.values.tolist()

            if len(list_header) != 13:
                messages.error(request, 'El archivo a cargar debe de tener 13 columnas')
                return render(request, 'fac/archexcel.html',{'form': form})

            #print (list_header)
            #Verifico que el orden d elas columnas coincidan
            if  list_header[0] !='NOMBRE RECEPTOR' or list_header[1] !='RFC' or list_header[2] != 'Folio' or list_header[3] != 'NOMBRE DE EMISOR' or list_header[4] != 'RFC EMISOR' or list_header[5] != 'TIPO DE DOCUMENTO' or list_header[6] != 'FECHA DE EMISION' or list_header[7] != 'MONEDA' or list_header[8] != 'ESTADO' or list_header[9] != 'SUBTOTAL' or list_header[10] != 'TOTAL' or list_header[11] != 'IVA' or list_header[12] != 'AFILIADO':
                messages.error(request, 'El archivo no tiene el orden de las columnas')
                return render(request, 'fac/archexcel.html',{'form': form})

            #Solo cargo de la 0 - 10 donde NO deben de haber nulos
            dbframe_nonull = dbframe.iloc[:,0:11] #Returns a new dataframe with first ten columns
            check_for_nan = dbframe_nonull.isnull().values.any()
            #print (check_for_nan)
            #print(dbframe_nonull)

            if (check_for_nan==True):
                messages.error(request, 'Hay valores nulos, verificar su archivo')
                return render(request, 'fac/archexcel.html',{'form': form})

            #Verifico las fechas. POSICION 6***********
            dbframe_fechas = dbframe.iloc[:, 6]

            if str(dbframe_fechas.dtype)[:4] != 'date':
               messages.error(request, 'Formato De Fechas NO es correcto!!!')
               return render(request, 'fac/archexcel.html',{'form': form})
            # ****************************

            for i in range(len(dbframe)):

                if Ereceptora.objects.filter(RFC=dbframe.iloc[i,1]).exists() == False:
                    #Receptor dbframe.iloc[i,0] dbframe.iloc[i,1]
                    obj_rec, created = Ereceptora.objects.filter(
                                Q(RFC=dbframe.iloc[i,1]),
                                ).get_or_create(RFC=dbframe.iloc[i,1], NOMBRE=dbframe.iloc[i,0], defaults={'usuario': vusername})


                #Receptor dbframe.iloc[i,3] dbframe.iloc[i,4]
                obj_emi, created = Eemisora.objects.filter(
                                Q(RFC=dbframe.iloc[i,4]),
                                ).get_or_create(RFC=dbframe.iloc[i,4], NOMBRE=dbframe.iloc[i,3], defaults={'usuario': vusername})

                #dbframe.iloc[i,5],
                obj_tipo_doc, created = TiposDoc.objects.filter(
                                Q(NOMBRE=dbframe.iloc[i,5]),
                                ).get_or_create(NOMBRE=dbframe.iloc[i,5], defaults={'usuario': vusername})

                obj_moneda, created = Monedas.objects.filter(
                                Q(NOMBRE=dbframe.iloc[i,7]),
                                ).get_or_create(NOMBRE=dbframe.iloc[i,7], defaults={'usuario': vusername})

                obj_edo_fac, created = EstadosFac.objects.filter(
                                Q(NOMBRE=dbframe.iloc[i,8]),
                                ).get_or_create(NOMBRE=dbframe.iloc[i,8], defaults={'usuario': vusername})                
                
                #Afiliado dbframe.iloc[i,12]
                # Como trae blancos evitamos los nan
                if dbframe.iloc[i,12] == dbframe.iloc[i,12]:

                    obj_afi, created = Afiliado.objects.filter(
                                Q(NOMBRE_ALIAS=dbframe.iloc[i,12]),
                                ).get_or_create(NOMBRE_ALIAS=dbframe.iloc[i,12], defaults={'usuario': vusername})
                else:
                    obj_afi, created = Afiliado.objects.filter(
                                Q(NOMBRE_ALIAS=""),
                                ).get_or_create(NOMBRE_ALIAS='', defaults={'usuario': vusername})

                V_ID_AFIL=obj_afi.ID_AFILIADO
 
                #Generamos las Facturas
                #"ID_EMISOR", "SERIE","FOLIO", "TIPO_DOCUMENTO"]
                V_FOLIO=dbframe.iloc[i,2]
                V_SERIE=V_FOLIO [ 0 ]

                #print (dbframe.iloc[i,6])
                #print (str(dbframe.iloc[i,6])[:10])
                V_FECHA_FAC=datetime.strptime( str(dbframe.iloc[i,6])[:10], '%Y-%m-%d')
                V_FECHA_FAC=V_FECHA_FAC.strftime('%Y-%m-%d')

                if dbframe.iloc[i,11] == dbframe.iloc[i,11]:
                    V_IVA = float (dbframe.iloc[i,11])
                else:
                    V_IVA = 0.0

                obj, created = Facturas.objects.filter(
                                Q(ID_EMISOR=obj_emi.ID_EMISOR) & Q(SERIE=V_SERIE) & Q(FOLIO=V_FOLIO),
                                ).get_or_create(ID_EMISOR      = Eemisora.objects.get(ID_EMISOR = obj_emi.ID_EMISOR),
                                                FOLIO          = V_FOLIO,
                                                SERIE          = V_SERIE,
                                                ID_TIPO_DOC    = TiposDoc.objects.get(ID_TIPO_DOC = obj_tipo_doc.ID_TIPO_DOC),    #dbframe.iloc[i,5],
                                                ID_RECEPTOR    = Ereceptora.objects.get(ID_RECEPTOR = obj_rec.ID_RECEPTOR),
                                                FECHA_EMISION  = V_FECHA_FAC,
                                                ID_MONEDA      = Monedas.objects.get(ID_MONEDA = obj_moneda.ID_MONEDA), #dbframe.iloc[i,7],
                                                ID_ESTADO_FAC  = EstadosFac.objects.get(ID_ESTADO_FAC = obj_edo_fac.ID_ESTADO_FAC), #dbframe.iloc[i,8],
                                                SUBTOTAL       = float (dbframe.iloc[i,9]),
                                                TOTAL          = float (dbframe.iloc[i,10]),
                                                IVA            = V_IVA,
                                                ID_AFILIADO    = Afiliado.objects.get(ID_AFILIADO = int (V_ID_AFIL)),
                                                TIPO_CAMBIO    = 0,
                                                defaults={'usuario': vusername})

            messages.error(request, 'Archivo cargado con éxito!!!!')
            return render(request, 'fac/archexcel.html',{'form': form})

    except Exception as identifier:
        print('identifier')
        print(identifier)
        form = CargaFacForm()

    form = CargaFacForm()
    return render(request, 'fac/archexcel.html',{'form': form})

# *********************************************************
# *********************************************************

def create_fac(request):  
    if request.method == "POST":  
        form = FacturaForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/create_fac')  
            except:  
                pass 
    else:  
        form = FacturaForm()  
    return render(request,'fac/create_fac.html',{'form':form})

#*************************************
#************************************


#***********************************
#***********************************

def list_fac_view(request):
    facturas = Facturas.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(facturas, 20)
    try:
        fac_list = paginator.page(page)
    except PageNotAnInteger:
        fac_list = paginator.page(1)
    except EmptyPage:
        fac_list = paginator.page(paginator.num_pages)

    return render(request, 'fac/list_fac.html', {'fac_list': fac_list})


@require_http_methods(['DELETE'])
def delete_fac(request, id):
    Facturas.objects.filter(ID_FACTURA=id).delete()
    facturas = Facturas.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(facturas, 20)
    try:
        fac_list = paginator.page(page)
    except PageNotAnInteger:
        fac_list = paginator.page(1)
    except EmptyPage:
        fac_list = paginator.page(paginator.num_pages)

    return render(request, 'fac/table_fac.html', {'fac_list': fac_list})

#***********************************
#***********************************

def find_fac(request):
    q = request.GET.get('query')

    if q:
        facturas = Facturas.objects.filter(FOLIO__icontains=q)
    else:
        facturas = Facturas.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(facturas, 20)
    try:
        fac_list = paginator.page(page)
    except PageNotAnInteger:
        fac_list = paginator.page(1)
    except EmptyPage:
        fac_list = paginator.page(paginator.num_pages)

    return render(request, 'fac/list_fac.html', {'fac_list': fac_list})

def find_fac_f(request):
    q = request.GET.get('query_f')

    if q:
        facturas = Facturas.objects.filter(FECHA_EMISION__icontains=q)
    else:
        facturas = Facturas.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(facturas, 20)
    try:
        fac_list = paginator.page(page)
    except PageNotAnInteger:
        fac_list = paginator.page(1)
    except EmptyPage:
        fac_list = paginator.page(paginator.num_pages)

    return render(request, 'fac/list_fac.html', {'fac_list': fac_list})

#*********************************
#*********************************


def update_fac(request):
    id = 1
    fac = Facturas.objects.get(id=id)
    context = {"fac": fac}
    return render(request, 'fac/update_fac.html', context)

class update_fac_view(View):

    def get(self, request, id):

        context_data = {"fac":Facturas.objects.get(id=id)}

        return render(request,'fac/update_fac.html',context_data)
