import logging.config
import logging

from django.shortcuts import render


def error(request):
    logging.getLogger('error_logger').info('--- erro404 ---')

    return render(request, 'error/error.html', {'number': '404', 'message': 'No Encontrado',
                                              'error': 'El servicio de autenticación no se encuentra disponible por el momento.'})
