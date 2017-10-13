import logging
import logging.config

from django.shortcuts import render

from apps.tvazteca.cabs.login.views import checkValue
from apps.tvazteca.cabs.coding.databases.connection import select
from apps.tvazteca.cabs.coding.query import queryListUser, queryListWitness
# Create your views here.


def startMetrics(request):
    logging.getLogger('info_logger').info('--- startMetrics ---')

    query = queryListUser()
    users = select(query, 'tvazteca_bloq')
    query = queryListWitness()
    witness = select(query, 'tvazteca_bloq')

    if checkValue(request):
        return render(request, 'metrics/metrics_general.html', {'users': users, 'witness': witness})
    else:
        return render(request, 'login/start_login.html', {
            'message_warning': 'Para visualizar las metricas del sistema favor de logearse primero.'})