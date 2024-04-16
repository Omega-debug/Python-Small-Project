from Service.AngajatService import AngajatService


class Consola:
    def __init__(self, angajatService: AngajatService):
        self.__angajatService = angajatService

    def adaugaAngajat(self):
        try:
            idAngajat = input("Dati id-ul angajatului: ")
            nume = input("Dati numele angajatului: ")
            CNP = input("Dati CNP-ul angajatului: ")
            self.__angajatService.adauga(idAngajat, nume, CNP)
        except KeyError as e:
            print(e)

    def modificaAngajat(self):
        try:

            idAngajat = input("Dati id-ul angajatului: ")
            numeNou = input("Dati noul nume al angajatului")
            CNPnou = input("Dati noul CNP al angajatului")
            self.__angajatService.modifica(idAngajat, numeNou, CNPnou)
        except KeyError as e:
            print(e)

    def stergeAngajat(self):
        try:

            idAngajat = input("Dati id-ul angajatului de sters")
            self.__angajatService.sterge(idAngajat)
        except KeyError as e:
            print(e)

    def afiseaza(self, entitati):
        for entitate in entitati:
            print(entitate)

    def printMeniu(self):
        print("1. Adauga angajat")
        print("2. Modifica angajat")
        print("3. Sterge angajat")
        print("a. Afiseaza toti angajatii")
        print("x. Iesire")

    def meniu(self):
        while True:
            self.printMeniu()
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.adaugaAngajat()
            elif optiune == "2":
                self.modificaAngajat()
            elif optiune == "3":
                self.stergeAngajat()
            elif optiune == "a":
                self.afiseaza(self.__angajatService.getAllAngajati())
            elif optiune == "x":
                break
            else:
                print("Optiune gresita, reincercati!")
