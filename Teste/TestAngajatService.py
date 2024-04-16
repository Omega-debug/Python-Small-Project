from Repository.AngajatRepository import AngajatRepository
from Service.AngajatService import AngajatService


def TestAdaugaAngajatService():
    angajatRepository = AngajatRepository()
    angajatService = AngajatService(angajatRepository)
    angajatService.adauga("5", "Andrei", "810")

    angajati = angajatService.getAllAngajati()
    assert len(angajati) == 1
    assert angajati[0].getIdAngajat() == "5"

    try:
        angajatService.adauga("5", "Marcel", "810")
        assert False
    except KeyError:
        ...


def TestModificaAngajatService():
    angajatRepository = AngajatRepository()
    angajatService = AngajatService(angajatRepository)
    angajatService.adauga("1", "Marcelus", "3002")
    angajatService.modifica("1", "Andrei", "2003")

    angajati = angajatService.getAllAngajati()
    assert angajati[0].getNume() == "Andrei"

    try:
        angajatService.modifica("2", "Gigel", "5006")
        assert False
    except KeyError:
        ...

def TestStergeAngajatService():
    angajatRepository = AngajatRepository()
    angajatService = AngajatService(angajatRepository)
    angajatService.adauga("1", "Smecheras", "3002")
    angajatService.sterge("1")
    angajati = angajatService.getAllAngajati()
    assert len(angajati) == 0

    try:
        angajatService.sterge("1")
        assert False
    except KeyError:
        ...

