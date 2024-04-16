class Angajat:
    def __init__(self, idAngajat, nume, CNP):
        self.__idAngajat = idAngajat
        self.__nume = nume
        self.__CNP = CNP

    def getIdAngajat(self):
        return self.__idAngajat

    def getNume(self):
        return self.__nume

    def getCNP(self):
        return self.__CNP

    def setIdAngajat(self, idAngajat):
        self.__idAngajat = idAngajat

    def setNume(self, nume):
        self.__nume = nume

    def setCNP(self, CNP):
        self.__CNP = CNP

    def __str__(self):
        return f"id: {self.__idAngajat}, nume: {self.__nume}, CNP: {self.__CNP}"