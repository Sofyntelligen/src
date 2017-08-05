import logging.config
import logging
import json

from django.http import HttpResponse

from apps.tvazteca.cabs.login.views import checkValue, ckackCounter
from apps.tvazteca.cabs.coding.util import *
from apps.tvazteca.cabs.coding.query import queyTableListWitness
from apps.tvazteca.cabs.coding.databases.connection import select, queryDLL
from django.shortcuts import render

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
    #dates = select(query, 'tvazteca_vidnotd')
    dates = select(query, 'tvazteca_bloq')

    for i in range(len(dates)):
        dates[i]['MUX'] = optionMux(dates[i]['MUX'])

    json_data = json.dumps(dates)

    return HttpResponse(json_data, content_type='application/json')

