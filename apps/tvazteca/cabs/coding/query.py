import logging
import logging.config
import time

from apps.tvazteca.cabs.coding.util import *


def queryTableViewFinder(type_network: str, type_error: str, level_alert: str, date_monitoring: str):
    date = formmatDate(date_monitoring)

    sql = 'SELECT ROWNUM AS NO, ' \
          'B.nombre_testigo AS NOMBRE, ' \
          'A.id_test AS ID, ' \
          'B.tipo_mux AS MUX, ' \
          'A.total_err_dur AS DURACION, ' \
          'A.total_err_ne AS NOLLEGAN, ' \
          'A.total_err_tam AS TAMANO, ' \
          'D.TOTAL, ' \
          'A.revisados AS REVISADOS, ' \
          'C.ULTIMO  ' \
          'FROM ' \
          'montest_concentrado_error A, ' \
          'lista_testigos B, ' \
          '(SELECT id_testigo, MAX(NUM_EV) AS ULTIMO FROM montest_detalle_error WHERE fecha = {date} GROUP BY id_testigo) C, ' \
          '(SELECT id_test, (total_err_dur + total_err_ne + total_err_tam) AS TOTAL FROM montest_concentrado_error WHERE fecha = {date}) D ' \
          'WHERE ' \
          'A.id_test = B.id_testigo AND ' \
          'B.id_testigo = C.id_testigo AND ' \
          'D.id_test = B.id_testigo '.format(date=date)

    if type_network != '1':
        if type_network == '2':
            sql = sql + 'AND B.grupo_testigos = 23 '
        elif type_network == '3':
            sql = sql + 'AND B.grupo_testigos = 24 '

    if type_error != '1':
        if type_error == '2':
            sql = sql + "AND A.total_err_dur > 0 "
        elif type_error == '3':
            sql = sql + "AND A.total_err_ne > 0 "
        elif type_error == '4':
            sql = sql + "AND A.total_err_tam > 0 "

    if level_alert != '1':
        if level_alert == '2':
            if type_error == '1':
                sql = sql + "AND D.TOTAL < 11 "
            if type_error == '2':
                sql = sql + "AND A.total_err_dur < 11 "
            elif type_error == '3':
                sql = sql + "AND A.total_err_ne < 11 "
            elif type_error == '4':
                sql = sql + "AND A.total_err_tam < 11 "

        elif level_alert == '3':
            if type_error == '1':
                sql = sql + "AND D.TOTAL >= 11 AND D.TOTAL <= 100 "
            if type_error == '2':
                sql = sql + "AND A.total_err_dur >= 11 AND A.total_err_dur <= 100 "
            elif type_error == '3':
                sql = sql + "AND A.total_err_ne >= 11 AND A.total_err_ne <= 100 "
            elif type_error == '4':
                sql = sql + "AND A.total_err_tam >= 11 AND A.total_err_tam <= 100 "

        elif level_alert == '4':
            if type_error == '1':
                sql = sql + "AND D.TOTAL > 100 "
            if type_error == '2':
                sql = sql + "AND A.total_err_dur > 100 "
            elif type_error == '3':
                sql = sql + "AND A.total_err_ne > 100 "
            elif type_error == '4':
                sql = sql + "AND A.total_err_tam > 100 "

    sql = sql + 'AND A.fecha = {date} ORDER BY NOMBRE ASC;'.format(date=date)

    logging.getLogger('info_logger').info('--- CONSULTA SQL --- ' + sql)

    return sql


def queryTableViewDetails(id_testigo: str, date_monitoring: str):
    date = formmatDate(date_monitoring)

    sql = 'SELECT ROWNUM AS NO, ' \
          'A.num_ev AS NUM_EVENTO, ' \
          'A.num_ev AS EVENTO, ' \
          'A.id_testigo AS ID, ' \
          'A.dur AS DURACION, ' \
          'A.tam AS TAMANO, ' \
          'A.tipo_err AS TIPO_ERROR, ' \
          'A.revisado AS REVISADO, ' \
          'B.nombre_testigo AS NOMBRE, ' \
          'B.ip_grabador AS IP, ' \
          'B.ruta_videos AS RUTA, ' \
          'B.nombre_usuario AS NOMBRE_USUARIO, ' \
          'B.tipo_guia AS TIPO_GUIA, ' \
          'B.grupo_testigos AS GRUPO_TESTIGO, ' \
          'B.tipo_mux AS MUX, ' \
          'B.siglas AS SIGLAS ' \
          'FROM ' \
          'montest_detalle_error A, ' \
          'lista_testigos B ' \
          'WHERE ' \
          'A.id_testigo = B.id_testigo AND ' \
          'A.id_testigo = {id} AND ' \
          'A.fecha = {date} ' \
          'ORDER BY NUM_EVENTO ASC;'.format(id=id_testigo, date=date)

    logging.getLogger('info_logger').info('--- CONSULTA SQL --- ' + sql)

    return sql


def queryDetailsUser(number: str):
    sql = 'SELECT ID, ' \
          'NUMERO_EMPLEADO, ' \
          'NOMBRE AS NOMBRE, ' \
          'PERMISOS AS PERMISOS, ' \
          'ACTIVO AS ACTIVO, ' \
          'PERFIL AS PERFIL ' \
          'FROM ' \
          'USUARIOS_SOPORTE_CABS ' \
          'WHERE ' \
          'NUMERO_EMPLEADO = {number};'.format(number=number)

    logging.getLogger('info_logger').info('--- CONSULTA SQL --- ' + sql)

    return sql


def queryCheckTestigoConcentrated(id_testigo: str, check: str, date_monitoring: str):
    date = formmatDate(date_monitoring)

    sql = 'UPDATE montest_concentrado_error SET revisados = {check} ' \
          'WHERE id_test = {id} and fecha = {date};'.format(id=id_testigo, date=date, check=check)

    logging.getLogger('info_logger').info('--- CONSULTA SQL UPDATE --- ' + sql)

    return sql


def queyChangeTestigoConcentrated(id_testigo: str, date_monitoring: str):
    date = formmatDate(date_monitoring)

    sql = 'SELECT REVISADOS ' \
          'FROM montest_concentrado_error ' \
          'WHERE id_test = {id} and fecha = {date};'.format(id=id_testigo, date=date)

    logging.getLogger('info_logger').info('--- CONSULTA SQL --- ' + sql)

    return sql


def queryCheckTestigoDetails(id_testigo: str, date_monitoring: str):
    date = formmatDate(date_monitoring)

    sql = 'UPDATE montest_detalle_error SET revisado = 1 ' \
          'WHERE id_testigo = {id} and fecha = {date};'.format(id=id_testigo, date=date)

    logging.getLogger('info_logger').info('--- CONSULTA SQL UPDATE  --- ' + sql)

    return sql


def queryChangeTestigoDetails(id_testigo: str, date_monitoring: str):
    date = formmatDate(date_monitoring)

    sql = 'SELECT COUNT(REVISADO) AS REVISADO ' \
          'FROM montest_detalle_error ' \
          'WHERE id_testigo = {id} and fecha = {date};'.format(id=id_testigo, date=date)

    logging.getLogger('info_logger').info('--- CONSULTA SQL --- ' + sql)

    return sql


def queryInsertBinnacle(id: str, operation: int, ip: str, employye: int, browser: int, so: int, data: str):
    id = time.strftime("%d%m%Y") + time.strftime("%H") + time.strftime("%M") + time.strftime("%S") + id.rjust(4, '0')

    sql = 'INSERT INTO ' \
          'BIT_INVENT_TESTIGOS(ID, OPERACION, IP, ID_USUARIO, NAVEGADOR, SO, DATOS) ' \
          'VALUES ' \
          '(\'{id}\', {operation}, \'{ip}\', {employye}, {browser}, {so}, \'{data}\');'.format(id=id,
                                                                                               operation=operation,
                                                                                               ip=ip, employye=employye,
                                                                                               browser=browser, so=so,
                                                                                               data=data)

    logging.getLogger('info_logger').info('--- CONSULTA SQL INSERT --- ' + sql)

    return sql


def queyTableListWitness(channel: int):
    sql = 'SELECT ROWNUM AS NO, ' \
          'ID_TESTIGO AS ID, ' \
          'NOMBRE_TESTIGO AS NOMBRE, ' \
          'TIPO_MUX AS MUX ' \
          'FROM ' \
          'LISTA_TESTIGOS ' \
          'WHERE '

    if channel == '0':
        condition = 'GRUPO_TESTIGOS=21 OR ' \
                    'GRUPO_TESTIGOS=22 OR ' \
                    'GRUPO_TESTIGOS=23 OR ' \
                    'GRUPO_TESTIGOS=24 OR ' \
                    'GRUPO_TESTIGOS=25 OR ' \
                    'GRUPO_TESTIGOS=26;'

    if channel == '1':
        condition = 'GRUPO_TESTIGOS=21 OR ' \
                    'GRUPO_TESTIGOS=23;'
    if channel == '2':
        condition = 'GRUPO_TESTIGOS=22 OR ' \
                    'GRUPO_TESTIGOS=24;'
    if channel == '3':
        condition = 'GRUPO_TESTIGOS=25;'

    if channel == '4':
        condition = 'GRUPO_TESTIGOS=26;'

    sql = sql + condition

    logging.getLogger('info_logger').info('--- CONSULTA SQL --- ' + sql)

    return sql


def querySubReport(type: int):
    sql = 'SELECT ' \
          'C.ID, C.SUB_REPORTE ' \
          'FROM ' \
          'CAT_REPORTES A, CAT_TIPO_REPORTE B, CAT_SUB_REPORTE C ' \
          'WHERE ' \
          'A.TIPO_REPORTE = B.ID AND A.SUB_REPORTE = C.ID AND A.TIPO_REPORTE = {type};'.format(type=type)

    logging.getLogger('info_logger').info('--- CONSULTA SQL --- ' + sql)

    return sql


def queryTypeReport():
    sql = 'SELECT * FROM CAT_TIPO_REPORTE;'

    logging.getLogger('info_logger').info('--- CONSULTA SQL --- ' + sql)

    return sql


def queryDataWitness(id: int):
    sql = 'SELECT ' \
          'ID_TESTIGO, NOMBRE_TESTIGO, TIPO_MUX ' \
          'FROM ' \
          'LISTA_TESTIGOS ' \
          'WHERE ' \
          'ID_TESTIGO = {id};'.format(id=id)

    logging.getLogger('info_logger').info('--- CONSULTA SQL --- ' + sql)

    return sql


def queryActionReport(id: int):
    sql = 'SELECT ' \
          'B.ID, B.ACCION ' \
          'FROM ' \
          'CAT_TIPO_REPORTE A, CAT_ACCIONES B, ACCIONES_REPORTES_TR C ' \
          'WHERE ' \
          'A.ID = C.TIPO_REPORTE AND B.ID = C.ACCION AND A.ID = {id};'.format(id=id)

    logging.getLogger('info_logger').info('--- CONSULTA SQL --- ' + sql)

    return sql


def queryCheckReports(id: int):
    sql = 'SELECT ' \
          'A.NUMERO_EMPLEADO AS EMPLEADO, ' \
          'A.NOMBRE AS NOMBRE, ' \
          'B.ID AS ID_REPORTE, ' \
          'B.FECHA AS FECHA, ' \
          'B.ID_TESTIGO AS ID_TESTIGO, ' \
          'C.ESTADO AS ESTADO, ' \
          'D.ID AS ID, ' \
          'E.ID AS ID_TIPO_REPORTE, ' \
          'E.TIPO_REPORTE, ' \
          'F.ID AS ID_SUB_REPORTE, ' \
          'F.SUB_REPORTE ' \
          'FROM ' \
          'USUARIOS_SOPORTE_CABS A, REPORTES_TESTIGOS B, CAT_ESTADOS C, CAT_REPORTES D, CAT_TIPO_REPORTE E, CAT_SUB_REPORTE F ' \
          'WHERE ' \
          'A.ID = B.ID_USUARIO AND B.ESTADO = C.ID AND B.REPORTE = D.ID AND D.TIPO_REPORTE = E.ID AND D.SUB_REPORTE = F.ID AND B.ID_TESTIGO = {id};'.format(
        id=id)

    logging.getLogger('info_logger').info('--- CONSULTA SQL --- ' + sql)

    return sql


def queryinsertReport(witness: int, id_user: int, report: int, state: int):
    id = time.strftime("%d%m%Y") + time.strftime("%H") + time.strftime("%M") + time.strftime("%S")

    sql = 'INSERT INTO REPORTES_TESTIGOS(ID, ID_TESTIGO, ID_USUARIO, REPORTE, ESTADO) VALUES({id}, {witness}, {id_user}, {report}, 1);'.format(
        id=id, witness=witness, id_user=id_user, report=report, state=state)

    logging.getLogger('info_logger').info('--- CONSULTA SQL --- ' + sql)

    return sql


def queryReportID(id_type_report: int, id_sub_report: int):
    sql = 'SELECT ' \
          'A.ID ' \
          'FROM ' \
          'CAT_REPORTES A, CAT_TIPO_REPORTE B, CAT_SUB_REPORTE C ' \
          'WHERE ' \
          'A.TIPO_REPORTE = B.ID AND A.SUB_REPORTE = C.ID AND A.TIPO_REPORTE = {id_type_report} AND A.SUB_REPORTE = {id_sub_report};'.format(
        id_type_report=id_type_report, id_sub_report=id_sub_report)

    logging.getLogger('info_logger').info('--- CONSULTA SQL --- ' + sql)

    return sql



