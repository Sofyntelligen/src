import logging
import logging.config

from django.db import connections


def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def select(query: str, databases: str):
    rows = ''

    try:
        querySQL = query
        cursor = connections[databases].cursor()
        cursor.execute(querySQL)
        connections[databases].commit()
        rows = dictfetchall(cursor)
        cursor.close()
    except:
        logging.getLogger('info_logger').error(
            '--- Error SQL - Datos no Insertados ---', querySQL)

    return rows


def queryDLL(query: str, databases: str):
    try:
        querySQL = query
        cursor = connections[databases].cursor()
        cursor.execute(querySQL)
        connections[databases].commit()
    except:
        logging.getLogger('info_logger').error(
            '--- Error SQL - Datos no Insertados ---', querySQL)

    return str(cursor.rowcount)
