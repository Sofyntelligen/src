import logging.config
import logging

from apps.tvazteca.cabs.login.views import checkValue, ckackCounter
from django.shortcuts import render

# Create your views here.


def startReportWitness(request):
    logging.getLogger('info_logger').info('--- startReportWitness ---')

    if checkValue(request):
        return render(request, 'report/witness.html')
    else:
        return render(request, 'login/start_login.html', {
                'message_warning': 'Para poder crear un reoprte de un testigo se necesita iniciar sesión'})



