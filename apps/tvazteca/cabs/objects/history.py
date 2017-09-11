class History:
    action = ''
    state = ''
    comment = ''
    user = ''
    date = ''

    def __init__(self):
        self.__type_report = ''
        self.__sub_report = ''
        self.__history = []

    def setTypeReport(self, type_report: str):
        self.__type_report = type_report

    def setSubReport(self, sub_report: str):
        self.__sub_report = sub_report

    def setHistory(self, history):
        self.__history = history

    def getHistory(self):
        return self.__history

    def addHistory(self):
        if self.action != 'FINALIZADO':
            self.state = 'ACTIVO'
        else:
            self.state = 'FINALIZADO'
        registry = {'TIPO_REPORTE': self.__type_report, 'SUB_REPORTE': self.__sub_report,
                    'ACCION': self.__notNull(self.action), 'ESTADO': self.state,
                    'COMENTARIO': self.__notNull(self.comment),
                    'NOMBRE': self.user, 'FECHA': self.date}
        self.__history.append(registry)
        if self.action is 'FINALIZADO':
            self.action = ''
            self.comment = ''

    def checkUpdateHistory(self, registry_update):
        if self.date == registry_update['FECHA']:
            if self.__typeUpdate(registry_update['TIPO']):
                self.__insertUpdateEquals(registry_update, True)
            else:
                self.__insertUpdateEquals(registry_update, False)
        else:
            if self.__typeUpdate(registry_update['TIPO']):
                self.__insertUpdateNotEquals(registry_update, True)
            else:
                self.__insertUpdateNotEquals(registry_update, False)

    def __insertUpdateNotEquals(self, registry_update, tarea):
        if tarea:
            self.addHistory()
            self.comment = registry_update['TAREA']
        else:
            self.addHistory()
            self.action = registry_update['TAREA']
        self.user = registry_update['NOMBRE']
        self.date = registry_update['FECHA']

    def __insertUpdateEquals(self, registry_update, tarea):
        if tarea:
            if registry_update['TAREA'] == self.comment or self.comment is '' or self.comment is 'N/A':
                self.comment = registry_update['TAREA']
            else:
                self.addHistory()
                self.comment = registry_update['TAREA']
        else:
            if registry_update['TAREA'] == self.action or self.action is '' or self.action is 'N/A':
                self.action = registry_update['TAREA']
            else:
                self.addHistory()
                self.action = registry_update['TAREA']

    def __notNull(self, data: str):
        if data == '':
            return 'N/A'
        else:
            return data

    def __typeUpdate(self, type: str):
        if type == 'COMENTARIO':
            return True
        if type == 'ACCION':
            return False
