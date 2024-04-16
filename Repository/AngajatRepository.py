class AngajatRepository:
    def __init__(self):
        self.__angajati = {}

    def getAll(self):
        '''
        retruneaza o lista de angajati
        :return: o lista de obiecte de tipul Angajat
        '''

        return list(self.__angajati.values())

    def getByID(self, idAngajat):
        '''
        returneaza angajatul cu id ul dat
        :param idAngajat: string
        :return: un obiect de tipul Angajat, daca exista unul cu id-ul dat, sau None in caz contrar
        '''

        if idAngajat in self.__angajati:
            return self.__angajati[idAngajat]
        return None

    def adauga(self, angajat):
        '''
        adauga un angajat in dictionar
        :param angajat: obiect de tipul Angajat
        :return:
        '''

        if self.getByID(angajat.getIdAngajat()) is not None:
            raise KeyError("exista deja un angajat cu id-ul dat!")
        self.__angajati[angajat.getIdAngajat] = angajat

    def modifica(self, angajatNou):
        '''
        modifica un angajat dupa id
        :param angajatNou: un obiect de tipul Angajat
        :return:
        '''

        if self.getByID(angajatNou.getIdAngajat()) is None:
            raise KeyError("Nu exista un angajat cu id-ul dat!")
        self.__angajati[angajatNou.getIdAngajat()] = angajatNou

    def sterge(self, idAngajat):
        '''
        sterge un angajat dupa id-ul dat
        :param idAngajat:
        :return:
        '''

        if self.getByID(idAngajat) is None:
            raise KeyError("Nu exista un angajat cu id-ul dat!")
        self.__angajati.pop(idAngajat)


