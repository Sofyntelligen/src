import json
import logging
import logging.config

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from apps.tvazteca.cabs.coding.databases.connection import select, queryDLL
from apps.tvazteca.cabs.coding.query import queryTypeReport, querySubReport, queryDataWitness, queryActionReport, \
    queryCheckReports, queryReportID, queryInsertReport, queryInsertComment, queryInsertAction, queryHistory, \
    queryUpdateReport, queryNumber
from apps.tvazteca.cabs.coding.util import *
from apps.tvazteca.cabs.login.views import checkValue
from apps.tvazteca.cabs.objects.history import History


# Create your views here.


def startReportWitness(request, id=None):
    logging.getLogger('info_logger').info('--- startReportWitness ---')

    if not checkValue(request):
        return render(request, 'login/start_login.html')

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
        reports = select(query, 'tvazteca_bloq')
        if reports:
            latest = len(reports) - 1
            if reports[latest]['ESTADO'] != 'FINALIZADO':
                request.session['id_report'] = reports[latest]['ID_REPORTE']
                id_state = reports[latest]['ID_ESTADO']
                id_type_report = reports[latest]['ID_TIPO_REPORTE']
                id_sub_report = reports[latest]['ID_SUB_REPORTE']

                if int(id_state) > 2:
                    if id_state == 3:
                        id_state = 0
                    if id_state == 4:
                        id_state = 1
                    if id_state == 5:
                        id_state = 2
                    if id_state == 6:
                        id_state = 3
                    request.session['id_state'] = id_state
                else:
                    id_state = -1
                    request.session['id_state'] = -1

                query = querySubReport(id_type_report)
                # datas = select(query, 'tvazteca_vidnotd')
                sub_report = select(query, 'tvazteca_bloq')

                query = queryActionReport(id_type_report)
                # datas = select(query, 'tvazteca_vidnotd')
                action_report = select(query, 'tvazteca_bloq')

                report = []
                comments = {}
                comment = ''
                report.append(reports[latest])
                history = evaluation_history(report)

                request.session['id_action'] = -1
                id_action = 0

                for i in range(len(history)):
                    if history[i]['COMENTARIO'] != 'N/A' and history[i]['COMENTARIO'] != comment:
                        comment = comments[history[i]['FECHA']] = history[i]['COMENTARIO']
                    if history[i]['ACCION'] != history[i]['ESTADO']:
                        for x in action_report:
                            if x['ACCION'] == history[i]['ACCION']:
                                 id_action = request.session['id_action'] = x['ID']

                details = reports[latest]['FECHA'].strftime('%d/%m/%Y - %H:%M:%S')
                details += ' por ' + reports[latest]['NOMBRE']
                return render(request, 'report/witness.html',
                              {'type_report': type_report, 'witness': witness, 'history': True, 'buttom': True,
                               'details': details, 'id_type_report': id_type_report, 'sub_report': sub_report,
                               'id_sub_report': id_sub_report, 'action_report': action_report, 'id_action': id_action,
                               'comments': comments, 'id_state': id_state,})
            else:
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
    logging.getLogger('info_logger').info('--- listHistory ---')

    if not checkValue(request):
        date = {"error": "error"}
        json_data = json.dumps(date)
        return HttpResponse(json_data, content_type='application/json')

    id_witness = request.GET.get('id_witness')

    query = queryCheckReports(id_witness)
    # datas = select(query, 'tvazteca_vidnotd')
    datas_report = select(query, 'tvazteca_bloq')

    history = evaluation_history(datas_report)

    json_data = json.dumps(history)

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

        try:
            rn = request.POST['option']
            if rn == '0':
                rn = 3
                red = 2
            if rn == '1':
                rn = 4
                red = 3
            if rn == '2':
                rn = 5
                red = 4
            if rn == '3':
                rn = 6
                red = 5
        except:
            rn = 1

        query = queryInsertReport(witness, id_user, report, rn)
        # dates = select(query, 'tvazteca_vidnotd')
        id_report = query['1']
        queryDLL(query['0'], 'tvazteca_bloq')

        action = request.POST['list_action_report']
        if '0' != action:
            query = queryInsertAction(id_user, id_report, action)
            # dates = select(query, 'tvazteca_vidnotd')
            queryDLL(query, 'tvazteca_bloq')

        comment = request.POST['commentArea']
        if comment:
            query = queryInsertComment(id_user, id_report, comment.upper())
            # dates = select(query, 'tvazteca_vidnotd')
            queryDLL(query, 'tvazteca_bloq')

        if rn != 1:
            query = queryInsertAction(id_user, id_report, red)
            # dates = select(query, 'tvazteca_vidnotd')
            queryDLL(query, 'tvazteca_bloq')

    return HttpResponseRedirect('/inventario_testigos/inicio/')


def updateReport(request, id_action=None, id_state=None, comment=None):
    logging.getLogger('info_logger').info('--- insertReportWitness ---')
    print(comment)
    id_user = request.session['id']
    id_report = request.session['id_report']

    if int(id_action) != int(request.session['id_action']):
        query = queryInsertAction(id_user, id_report, id_action)
        # dates = select(query, 'tvazteca_vidnotd')
        queryDLL(query, 'tvazteca_bloq')

    if comment != 'null':
        query = queryInsertComment(id_user, id_report, comment.upper())
        # dates = select(query, 'tvazteca_vidnotd')
        queryDLL(query, 'tvazteca_bloq')

    if int(id_state) != int(request.session['id_state']):
        query = queryUpdateReport(int(id_state) + 3, id_report)
        # dates = select(query, 'tvazteca_vidnotd')
        queryDLL(query, 'tvazteca_bloq')

        query = queryInsertAction(id_user, id_report, int(id_state) + 2)
        # dates = select(query, 'tvazteca_vidnotd')
        queryDLL(query, 'tvazteca_bloq')

    return HttpResponseRedirect('/inventario_testigos/inicio/')


def endReport(request, id_action=None, id_state=None, comment=None):
    logging.getLogger('info_logger').info('--- insertReportWitness ---')

    id_user = request.session['id']
    id_report = request.session['id_report']

    query = queryUpdateReport(2, id_report)
    # dates = select(query, 'tvazteca_vidnotd')
    queryDLL(query, 'tvazteca_bloq')

    if int(id_action) != int(request.session['id_action']):
        query = queryInsertAction(id_user, id_report, id_action)
        # dates = select(query, 'tvazteca_vidnotd')
        queryDLL(query, 'tvazteca_bloq')

    if comment != 'null':
        query = queryInsertComment(id_user, id_report, comment.upper())
        # dates = select(query, 'tvazteca_vidnotd')
        queryDLL(query, 'tvazteca_bloq')

    if int(id_state) != int(request.session['id_state']):
        query = queryInsertAction(id_user, id_report, int(id_state) + 2)
        # dates = select(query, 'tvazteca_vidnotd')
        queryDLL(query, 'tvazteca_bloq')

    query = queryInsertAction(id_user, id_report, 1)
    # dates = select(query, 'tvazteca_vidnotd')
    queryDLL(query, 'tvazteca_bloq')

    return HttpResponseRedirect('/inventario_testigos/inicio/')


def evaluation_history(datas_report):
    logging.getLogger('info_logger').info('--- evaluation_history ---')
    history = History()

    for i in range(len(datas_report)):
        id_report = datas_report[i]['ID_REPORTE']

        history.setTypeReport(datas_report[i]['TIPO_REPORTE'])
        history.setSubReport(datas_report[i]['SUB_REPORTE'])
        history.state = datas_report[i]['ESTADO']
        history.user = datas_report[i]['NOMBRE']
        history.date = datas_report[i]['FECHA'].strftime('%d/%m/%Y - %H:%M:%S')

        query = queryHistory(id_report)
        # datas = select(query, 'tvazteca_vidnotd')
        data_history = select(query, 'tvazteca_bloq')

        if data_history:
            for x in range(len(data_history)):
                data_history[x]['FECHA'] = data_history[x]['FECHA'].strftime('%d/%m/%Y - %H:%M:%S')
                history.checkUpdateHistory(data_history[x])
            history.addHistory()
        else:
            history.addHistory()

        history.comment = ''
        history.action = ''

    print(data_history)
    return history.getHistory()
