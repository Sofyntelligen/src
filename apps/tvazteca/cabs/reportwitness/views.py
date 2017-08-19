import json
import logging
import logging.config

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from apps.tvazteca.cabs.coding.databases.connection import select, queryDLL
from apps.tvazteca.cabs.coding.query import queryTypeReport, querySubReport, queryDataWitness, queryActionReport, \
    queryCheckReports, queryReportID, queryinsertReport
from apps.tvazteca.cabs.coding.util import *
from apps.tvazteca.cabs.login.views import checkValue


# Create your views here.


def startReportWitness(request, id=None):
    logging.getLogger('info_logger').info('--- startReportWitness ---')

    request.session['witness'] = id

    if checkValue(request):
        query = queryTypeReport()
        # type_report = select(query, 'tvazteca_vidnotd')
        type_report = select(query, 'tvazteca_bloq')
        query = queryDataWitness(id)
        # witness = select(query, 'tvazteca_vidnotd')
        witness = select(query, 'tvazteca_bloq')
        witness[0]['TIPO_MUX'] = optionMux(witness[0]['TIPO_MUX'])
        query = queryCheckReports(id)
        report = select(query, 'tvazteca_bloq')
        if report:
            print(report)
            return render(request, 'report/witness.html',
                          {'type_report': type_report, 'witness': witness, 'history': True})
        else:
            return render(request, 'report/witness.html', {'type_report': type_report, 'witness': witness})
    else:
        return render(request, 'login/start_login.html', {
            'message_warning': 'Para poder crear un reporte de un testigo se necesita iniciar sesión'})


def listSubReportJSON(request):
    logging.getLogger('info_logger').info('--- listSubReportJSON ---')

    if not checkValue(request):
        date = {"error": "error"}
        json_data = json.dumps(date)
        return HttpResponse(json_data, content_type='application/json')

    type = request.GET.get('type')

    if type == 0:
        return HttpResponse({}, content_type='application/json')

    query = querySubReport(type)
    # datas = select(query, 'tvazteca_vidnotd')
    datas = select(query, 'tvazteca_bloq')

    json_data = json.dumps(datas)

    return HttpResponse(json_data, content_type='application/json')


def listActionReportJSON(request):
    logging.getLogger('info_logger').info('--- listActionReportJSON ---')

    if not checkValue(request):
        date = {"error": "error"}
        json_data = json.dumps(date)
        return HttpResponse(json_data, content_type='application/json')

    type = request.GET.get('type')

    if type == 0:
        return HttpResponse({}, content_type='application/json')

    query = queryActionReport(type)
    # datas = select(query, 'tvazteca_vidnotd')
    datas = select(query, 'tvazteca_bloq')

    json_data = json.dumps(datas)

    return HttpResponse(json_data, content_type='application/json')

def listHistory(request):
    id_witness = request.GET.get('id_witness')

    query = queryCheckReports(id_witness)
    # datas = select(query, 'tvazteca_vidnotd')
    datas = select(query, 'tvazteca_bloq')
    print(datas)
    datas[0]['FECHA'] = datas[0]['FECHA'].strftime('%d/%m/%Y - %H:%M:%S')
    datas[0]['ACCION'] = 'N/A'
    datas[0]['COMENTARIO'] = 'N/A'

    json_data = json.dumps(datas)

    return HttpResponse(json_data, content_type='application/json')

def insertReportWitness(request):
    logging.getLogger('info_logger').info('--- insertReportWitness ---')

    if not checkValue(request):
        return render(request, 'login/start_login.html')

    if request.method == 'POST':
        id_user = request.session['id']
        witness = request.session['witness']
        query = queryReportID(request.POST['list_type_report'], request.POST['list_sub_report'])
        # dates = select(query, 'tvazteca_vidnotd')
        data = select(query, 'tvazteca_bloq')
        report = data[0]['ID']
        action = request.POST['list_action_report']
        try:
            rn = request.POST['option']
        except:
            rn = 0
        comment = request.POST['commentArea']

        query = queryinsertReport(witness, id_user, report, 1)
        # dates = select(query, 'tvazteca_vidnotd')
        queryDLL(query, 'tvazteca_bloq')

    return HttpResponseRedirect('/inventario_testigos/inicio/')
