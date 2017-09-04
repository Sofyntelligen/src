import json
import logging
import logging.config

from django.http import HttpResponse
from django.shortcuts import render

from apps.tvazteca.cabs.coding.databases.connection import select
from apps.tvazteca.cabs.coding.query import queyTableListWitness, queryCheckReports
from apps.tvazteca.cabs.coding.util import *
from apps.tvazteca.cabs.login.views import checkValue


# Create your views here.


def startViewTracing(request):
    logging.getLogger('info_logger').info('--- startViewTracing ---')

    if checkValue(request):
        return render(request, 'tracing/start_tracing.html')
    else:
        return render(request, 'login/start_login.html', {
            'message_warning': 'Para poder realizar una consulta en el inventario de Testigos. Es necesario Iniciar Sesión'})


def dateTableTracingJSON(request):
    logging.getLogger('info_logger').info('--- dateTableTracingJSON ---')

    if not checkValue(request):
        date = {"error": "error"}
        json_data = json.dumps(date)
        return HttpResponse(json_data, content_type='application/json')

    type_network = request.GET.get('type_network')

    query = queyTableListWitness(type_network)
    # datas = select(query, 'tvazteca_vidnotd')
    datas = select(query, 'tvazteca_bloq')

    for i in range(len(datas)):
        datas[i]['MUX'] = optionMux(datas[i]['MUX'])
        if datas[i]['ID_REPORTE'] is None:
            datas[i]['ID_REPORTE'] = 0
    json_data = json.dumps(datas)
    print(datas)

    return HttpResponse(json_data, content_type='application/json')
