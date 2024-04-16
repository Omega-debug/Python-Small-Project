from Repository.AngajatRepository import AngajatRepository
from domain.angajat import Angajat


class AngajatService:
    def __init__(self, angajatRepository: AngajatRepository):
        self.__angajatRepository = angajatRepository

    def getAllAngajati(self):
        '''
        returneaza lista de angajati
        :return: o lista dee obiecte de tipul Angajat
        '''

        return self.__angajatRepository.getAll()

    def adauga(self, idAngajat, nume, CNP):
        '''
        adauga un angajat
        :param idAngajat: string
        :param nume: string
        :param CNP: string
        :return:
        '''

        angajat = Angajat(idAngajat, nume, CNP)
        self.__angajatRepository.adauga(angajat)

    def modifica(self, idAngajatNou, numeNou, CNPnou):
        '''
        modifica un angajat
        :param idAngajatNou: string
        :param numeNou: string
        :param CNPnou: string
        :return:
        '''

        angajatNou = Angajat(idAngajatNou, numeNou, CNPnou)
        self.__angajatRepository.modifica(angajatNou)

    def sterge(self, idAngajat):
        '''
        sterge un obiect de tipul angajat
        :param idAngajat:
        :return:
        '''

        self.__angajatRepository.sterge(idAngajat)
