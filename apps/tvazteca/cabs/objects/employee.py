class Employee:
    def __init__(self, name: str, email: str, number_employee: str, business: str, marketstall: str, id_user: str):
        self.name = name
        self.email = email
        self.number_employee = number_employee
        self.business = business
        self.marketstall = marketstall
        self.id_user = id_user

    def getName(self):
        return self.name

    def setName(self, name: str):
        self.name = name

    def getEmail(self):
        return self.email

    def setEmail(self, email: str):
        self.email = email

    def getNumber_employee(self):
        return self.number_employee

    def setNumber_employee(self, number_employee: str):
        self.number_employee = number_employee

    def getBusiness(self):
        return self.business

    def setBusiness(self, business: str):
        self.business = business

    def getMarketstall(self):
        return self.marketstall

    def setMarketstall(self, marketstall: str):
        self.marketstall = marketstall

    def getId_user(self):
        return self.id_user

    def setId_user(self, id_user: str):
        self.id_user = id_user



