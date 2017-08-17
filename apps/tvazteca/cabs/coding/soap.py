from suds.client import Client

from apps.tvazteca.cabs.coding.util import subString


class Soap:
    url = 'http://10.50.169.89/wsapploginparam/service.asmx?wsdl'

    def __init__(self, employee: str, password: str):
        self.employee = employee
        self.password = password

    def accessLogin(self):
        client = Client(self.url)
        result = client.service.gsc_llave(self.employee, self.password, '58')
        data = result.split("\" ")
        date_result = []

        if 1 == len(data):
            return {'result': '[Fail]'}
        else:
            for x in range(9):
                date_result.insert(x, subString(data[x], '\"'))
            if '[OK]' == date_result[8]:
                return {'result': '[Ok]', 'employee': date_result}
            else:
                return {'result': '[Error]'}
