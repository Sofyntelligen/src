import logging
import logging.config

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from apps.tvazteca.cabs.coding.encryption import Encryption
from apps.tvazteca.cabs.coding.query import queryDetailsUser, queryInsertBinnacle
from apps.tvazteca.cabs.coding.databases.connection import select, queryDLL
from apps.tvazteca.cabs.coding.soap import Soap
from apps.tvazteca.cabs.login.form import Login
from apps.tvazteca.cabs.coding.databases.datas import getBrowser, getSO

# Create your views here. https://github.com/sivaa/django-jquery-ajax-exmaples/tree/master/django-jquery-ajax/templates

def startLogin(request):
    logging.getLogger('info_logger').info('--- startLogin ---')

    if checkValue(request):
        return HttpResponseRedirect('inventario_testigos/monitoreo_testigos/')
    else:
        return render(request, 'login/start_login.html')


@csrf_exempt
def evaluationLogin(request):
    logging.getLogger('info_logger').info('--- evaluationLogin ---')

    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            inputEmployee = form.cleaned_data['inputEmployee']
            inputPassword = form.cleaned_data['inputPassword']

            encryption = Encryption()
            encryption.setData(inputEmployee)
            inputEmployee = encryption.getEncryption()
            encryption.setData(inputPassword)
            inputPassword = encryption.getEncryption()

            browser = getBrowser(request)
            os = getSO(request)
            ip = request.META['REMOTE_ADDR']
            counter = str(ckackCounter(request))

            try:
                resultSoap = Soap(inputEmployee, inputPassword)
                soap = resultSoap.accessLogin()
                result = soap['result']
            except:
                logging.getLogger('error_logger').info(
                    '--- Error 404 - El servicio de autenticación no se encuentra disponible por el momento. ---')
                return render(request, 'error/error.html', {'number': '404', 'message': 'No Encontrado',
                                                            'error': 'El servicio de autenticación no se encuentra disponible por el momento'})
            #print(request.META)
            if '[Ok]' == result:
                query = queryDetailsUser(soap['employee'][2])
                #details = select(query, 'tvazteca_bloq')
                details = select(query, 'tvazteca_bloq')
                if len(details) == 1:
                    if details[0]['ACTIVO'] == 0:
                        request.session['sessionStart'] = True
                        request.session['name'] = details[0]['NOMBRE']
                        request.session['email'] = soap['employee'][1]
                        request.session['number_employee'] = soap['employee'][2]
                        request.session['business'] = soap['employee'][3]
                        request.session['marketstall'] = details[0]['PERFIL']
                        request.session['id_user'] = soap['employee'][5]
                        request.session['permission'] = details[0]['PERMISOS']
                        request.session['active'] = details[0]['ACTIVO']
                        request.session['id'] = details[0]['ID']
                        request.session.set_expiry(1800)
                        query = queryInsertBinnacle(counter,  1, ip, int(request.session['id']), browser, os, '')
                        #queryDLL(query, 'tvazteca_bloq')
                        queryDLL(query, 'tvazteca_bloq')
                        return HttpResponseRedirect('inicio/')
                    else:
                        query = queryInsertBinnacle(counter, 6, ip, 1, browser, os, '')
                        #queryDLL(query, 'tvazteca_bloq')
                        queryDLL(query, 'tvazteca_bloq')
                        logging.getLogger('error_logger').info('--- El Usuario. No esta activo por lo tanto no tiene acceso al sistema, Verificar su acceso ---')
                        return render(request, 'login/start_login.html',
                                      {'message_warning': 'El Usuario. No esta activo por lo tanto no tiene acceso al sistema, Verificar su acceso'})
                else:
                    query = queryInsertBinnacle(counter, 5, ip, 1, browser, os, '')
                    #queryDLL(query, 'tvazteca_bloq')
                    queryDLL(query, 'tvazteca_bloq')
                    logging.getLogger('error_logger').info('--- El Usuario. No cuenta con privilegios para entrar ---')
                    return render(request, 'login/start_login.html',
                                  {'message_warning': 'El Usuario. No cuenta con privilegios para entrar'})
            elif '[Error]' == result:
                query = queryInsertBinnacle(counter, 4, ip, 1, browser, os, '')
                #queryDLL(query, 'tvazteca_bloq')
                queryDLL(query, 'tvazteca_bloq')
                logging.getLogger('error_logger').info('--- Contraseña incorrecta. Verficar ---')
                return render(request, 'login/start_login.html', {'message_error': 'Contraseña incorrecta. Verficar'})
            elif '[Fail]' == result:
                query = queryInsertBinnacle(counter, 3, ip, 1, browser, os, '')
                #queryDLL(query, 'tvazteca_bloq')
                queryDLL(query, 'tvazteca_bloq')
                logging.getLogger('error_logger').info('--- Usuario y Contraseña incorrectos. Verficar ---')
                return render(request, 'login/start_login.html',
                              {'message_error': 'Usuario y Contraseña incorrectos. Verficar'})

    return render(request, 'login/start_login.html')


def closeSession(request):
    logging.getLogger('info_logger').info('--- closeSession ---')

    if not checkValue(request):
        return render(request, 'login/start_login.html')

    try:
        del request.session['sessionStart']
        id = int(request.session['id'])
        del request.session['name']
        del request.session['email']
        del request.session['number_employee']
        del request.session['business']
        del request.session['marketstall']
        del request.session['id_user']
        del request.session['permission']
        del request.session['active']
        del request.session['id']

        browser = getBrowser(request)
        os = getSO(request)
        ip = request.META['REMOTE_ADDR']
        counter = str(ckackCounter(request))

        query = queryInsertBinnacle(counter, 2, ip, id, browser, os, '')
        #queryDLL(query, 'tvazteca_bloq')
        queryDLL(query, 'tvazteca_bloq')
    except:
        logging.getLogger('error_logger').info(
           '--- Error 404 - El servicio de autenticación no se encuentra disponible por el momento. ---')
        return render(request, 'error/error.html', {'number': '400', 'message': 'Solicitud Incorrecta',
                                                    'error': 'Actualmente usted no tiene una sesión iniciada o se cerro su sesión por inactividad. Inicie Sesión'})

    logging.getLogger('info_logger').info('--- Session Cerrada ---')

    return render(request, 'login/start_login.html', {'message_info': 'Vuelva Pronto.'})


def checkValue(request):
    try:
        if request.session['sessionStart']:
            return True
        else:
            return False
    except:
        return False


def ckackCounter(request):
    try:
        if request.session['counter']:
            request.session['counter'] = int(request.session['counter']) + 1
            return request.session['counter']
        else:
            request.session['counter'] = 1
            return request.session['counter']
    except:
        request.session['counter'] = 1
        return request.session['counter']

