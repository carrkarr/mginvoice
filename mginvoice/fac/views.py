from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import redirect
from django.template import RequestContext
from django.shortcuts import render
from fac.forms import CargaFacForm

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
        #and request.FILES['myfile']
        if request.method == 'POST':

            form = CargaFacForm(request.POST)
            vusername = request.user  # Obtengo el usuario de la sesion y lo asigno a la variable para ser salvado.

            # Esta funciona y valida que se teclee algo en la pantalla
            myfile = request.FILES.get("docfile", "Guest")

            #Si trae caracteres raros no subira el archivo
            try:
                #empexceldata = pd.read_csv("."+myfile,encoding='utf-8')
                empexceldata = pd.read_csv(myfile, encoding='utf-8')
            except Exception as identifier:
                messages.error(request, 'Hay caracteres raros, verificar su archivo')
                return render(request, 'fac/archexcel.html',{'form': form})

            #empexceldata = pd.read_csv(myfile)

            dbframe = empexceldata

            #Solo cargo de la 0 - 10 donde NO deben de haber nulos
            dbframe_nonull = dbframe.iloc[:,0:11] #Returns a new dataframe with first ten columns
            check_for_nan = dbframe_nonull.isnull().values.any()
            #print (check_for_nan)
            #print(dbframe_nonull)

            if (check_for_nan==True):
                messages.error(request, 'Hay valores nulos, verificar su archivo')
                return render(request, 'fac/archexcel.html',{'form': form})

            dbframe.to_csv(header=None,index=False)

            for i in range(len(dbframe)):
                #Receptor dbframe.iloc[i,0] dbframe.iloc[i,1]
                obj_rec, created = Ereceptora.objects.filter(
                                Q(RFC=dbframe.iloc[i,1]),
                                ).get_or_create(RFC=dbframe.iloc[i,1], NOMBRE=dbframe.iloc[i,0], defaults={'usuario': vusername})

                #Receptor dbframe.iloc[i,3] dbframe.iloc[i,4]
                obj_emi, created = Eemisora.objects.filter(
                                Q(RFC=dbframe.iloc[i,4]),
                                ).get_or_create(RFC=dbframe.iloc[i,4], NOMBRE=dbframe.iloc[i,3], defaults={'usuario': vusername})


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
                #V_FOLIO=V_FOLIO[1:]

                V_FECHA_FAC=datetime.strptime(dbframe.iloc[i,6], '%d/%m/%Y')
                V_FECHA_FAC=V_FECHA_FAC.strftime('%Y-%m-%d')

                if dbframe.iloc[i,11] == dbframe.iloc[i,11]:
                    V_IVA = float (dbframe.iloc[i,11])
                else:
                    V_IVA = 0.0

                obj, created = Facturas.objects.filter(
                                Q(ID_EMISOR=obj_emi.ID_EMISOR) & Q(SERIE=V_SERIE) & Q(FOLIO=V_FOLIO) & Q(ESTADO_FACTURA=dbframe.iloc[i,8]),
                                ).get_or_create(ID_EMISOR      = Eemisora.objects.get(ID_EMISOR = obj_emi.ID_EMISOR),
                                                FOLIO          = V_FOLIO,
                                                SERIE          = V_SERIE,
                                                TIPO_DOCUMENTO = dbframe.iloc[i,5],
                                                ID_RECEPTOR    = Ereceptora.objects.get(ID_RECEPTOR = obj_rec.ID_RECEPTOR),
                                                FECHA_EMISION  = V_FECHA_FAC,
                                                MONEDA         = dbframe.iloc[i,7],
                                                ESTADO_FACTURA = dbframe.iloc[i,8],
                                                SUBTOTAL       = float (dbframe.iloc[i,9]),
                                                TOTAL          = float (dbframe.iloc[i,10]),
                                                IVA            = V_IVA,
                                                ID_AFILIADO    = Afiliado.objects.get(ID_AFILIADO = int (V_ID_AFIL)),
                                                TIPO_CAMBIO    = 0,
                                                defaults={'usuario': vusername})

            messages.error(request, 'Archivo cargado con éxito!!!!')
            return render(request, 'fac/archexcel.html',{'form': form})

    except Exception as identifier:
        #print(identifier)
        form = CargaFacForm()

    form = CargaFacForm()
    return render(request, 'fac/archexcel.html',{'form': form})
