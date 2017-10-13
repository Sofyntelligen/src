import json
import logging
import logging.config
from wsgiref.util import FileWrapper

from django.http import HttpResponse
from django.shortcuts import render

from apps.tvazteca.cabs.coding.databases.connection import select, queryDLL
from apps.tvazteca.cabs.coding.databases.datas import getBrowser, getSO
from apps.tvazteca.cabs.coding.query import queryTableViewFinder, queryTableViewDetails, queryCheckTestigoConcentrated, \
    queryCheckTestigoDetails, queryInsertBinnacle, queryChangeTestigoDetails
from apps.tvazteca.cabs.coding.util import *
from apps.tvazteca.cabs.login.views import checkValue, ckackCounter


# Create your views here.
# SA or UVI

def startViewFinderWeb(request):
    logging.getLogger('info_logger').info('--- startViewFinderWeb ---')

    if checkValue(request):
        return render(request, 'viewfinderweb/start_viewfinderweb.html')
    else:
        return render(request, 'login/start_login.html', {
            'message_warning': 'Para poder realizar una consulta en el Monitor Automático de Testigos. Es necesario Iniciar Sesión'})


def dateTableViewFinderJSON(request):
    logging.getLogger('info_logger').info('--- dateTableViewFinderJSON ---')

    if not checkValue(request):
        date = {"error": "error"}
        json_data = json.dumps(date)
        return HttpResponse(json_data, content_type='application/json')

    type_network = request.GET.get('type_network')
    type_error = request.GET.get('type_error')
    level_alert = request.GET.get('level_alert')
    date_monitoring = request.GET.get('date_monitoring')

    query = queryTableViewFinder(type_network, type_error, level_alert, date_monitoring)
    dates = select(query, 'tvazteca_vidnotd')
    #dates = select(query, 'tvazteca_bloq')

    for i in range(len(dates)):
        dates[i]['MUX'] = optionMux(dates[i]['MUX'])
        dates[i]['ULTIMO'] = formattTimeSecond(dates[i]['ULTIMO'])

    json_data = json.dumps(dates)

    return HttpResponse(json_data, content_type='application/json')


def dateTableViewDetailsJSON(request):
    logging.getLogger('info_logger').info('--- dateTableViewDetailsJSON ---')

    if not checkValue(request):
        date = {"error": "error"}
        json_data = json.dumps(date)
        return HttpResponse(json_data, content_type='application/json')

    id_testigo = request.GET.get('id_testigo')
    date_monitoring = request.GET.get('date_monitoring')

    query = queryTableViewDetails(id_testigo, date_monitoring)
    dates = select(query, 'tvazteca_vidnotd')
    #dates = select(query, 'tvazteca_bloq')

    for i in range(len(dates)):
        dates[i]['NUM_EVENTO'] = formattTimeSecond(dates[i]['NUM_EVENTO'])
        duration = dates[i]['DURACION']
        if duration == -1:
            dates[i]['DURACION'] = '00:00:00'
        else:
            dates[i]['DURACION'] = formattTimeMinute(duration)
        dates[i]['TAMANO'] = converterBytes(dates[i]['TAMANO'])
        type_error = dates[i]['TIPO_ERROR']
        if type_error == 1:
            dates[i]['TIPO_ERROR'] = 'DURACIÓN'
        elif type_error == 2:
            dates[i]['TIPO_ERROR'] = 'TAMAÑO'
        elif type_error == 3:
            dates[i]['TIPO_ERROR'] = 'NO EXISTE'
        reviewed = dates[i]['REVISADO']
        if reviewed == 0:
            dates[i]['REVISADO'] = 'NO'
        else:
            dates[i]['REVISADO'] = 'SI'

    json_data = json.dumps(dates)

    return HttpResponse(json_data, content_type='application/json')


def dateCheck(request):
    logging.getLogger('info_logger').info('--- dateCheck ---')

    if not checkValue(request):
        date = {"error": "error"}
        json_data = json.dumps(date)
        return HttpResponse(json_data, content_type='application/json')

    id_testigo = request.GET.get('id_testigo')
    check = request.GET.get('check')
    date_monitoring = request.GET.get('date_monitoring')

    query = queryChangeTestigoDetails(id_testigo, date_monitoring)
    number = select(query, 'tvazteca_bloq')
    datas = 'ACTUALIZACION, montest_concentrado_error(REVISADOS: 0, {check}) ' \
            'montest_detalle_error(REVISADO: 0,1) {number}  :  ' \
            'id_tesgigo: {id}, fecha {date}'.format(check=check, number=number[0]['REVISADO'], id=id_testigo,
                                                    date=date_monitoring)

    query = queryCheckTestigoConcentrated(id_testigo, check, date_monitoring)
    result1 = queryDLL(query, 'tvazteca_vidnotd')
    #result1 = queryDLL(query, 'tvazteca_bloq')
    query = queryCheckTestigoDetails(id_testigo, date_monitoring)
    result2 = queryDLL(query, 'tvazteca_vidnotd')
    #result2 = queryDLL(query, 'tvazteca_bloq')

    id = int(request.session['id'])
    browser = getBrowser(request)
    os = getSO(request)
    ip = request.META['REMOTE_ADDR']
    counter = str(ckackCounter(request))

    query = queryInsertBinnacle(counter, 7, ip, id, browser, os, datas)
    # queryDLL(query, 'tvazteca_bloq')
    queryDLL(query, 'tvazteca_bloq')

    date = {"result1": result1, "result2": result2}
    json_data = json.dumps(date)

    return HttpResponse(json_data, content_type='application/json')


def getUrlMedia(request, id=None, date=None, event=None, url=None, name=None):
    logging.getLogger('info_logger').info('--- getUrlMeida ---')

    date_format = date.split('-')

    if int(id) > 99:
        id_format = id.rjust(4, '0')
    else:
        id_format = id.rjust(2, '0')

    url_media = '/media/testigos' + name + '/' + url + '/' + completeNumber(date_format[0]) + '_' + completeNumber(
        date_format[1]) + '_' + date_format[2] + '/' + id_format + completeNumber(date_format[0]) + completeNumber(
        date_format[1]) + date_format[2][2] + date_format[2][3] + event.rjust(8, '0') + '.mp4'
    try:
        file = FileWrapper(open(url_media, 'rb'))
    except:
        return render(request, 'error/error.html', {'number': '404', 'message': 'No Encontrado',
                                                    'error': 'El video a descargar no se encuentra disponible o no existe.'})
    response = HttpResponse(file, content_type='video/mp4')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(
        id_format + completeNumber(date_format[0]) + completeNumber(date_format[1]) + date_format[2][2] +
        date_format[2][3] + event.rjust(8, '0') + '.mp4')

    logging.getLogger('info_logger').info('--- video descargado ---' + url_media)

    return response
