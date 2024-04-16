from Repository.AngajatRepository import AngajatRepository
from domain.angajat import Angajat


def testAdaugaAngajatRepository():
    angajatRepository = AngajatRepository()
    angajat = Angajat("1", "Diana", "314")
    angajatRepository.adauga(angajat)
    angajati = angajatRepository.getAll()
    assert len(angajati) == 1
    assert angajati[0].getIdAngajat() == "1"

  #  try:
        #angajatRepository.adauga(angajat)
       #assert False
#    except KeyError:
        #...

def testModificaAngajatRepository():
    angajatRepository = AngajatRepository()
    angajat = Angajat("2", "Maria", "512")
    angajatRepository.adauga(angajat)
    angajatNou1 = Angajat("2", "Mihnea", "220")
    angajatNou2 = Angajat("3", "Edi", "1")
    angajatRepository.modifica(angajatNou1)

    angajati = angajatRepository.getAll()
    assert angajati[0].getNume() == "Mihnea"
    assert angajati[0].getCNP() == "220"

    try:
        angajatRepository.modifica(angajatNou2)
        assert False
    except KeyError:
        ...

def testStergeAngajatRepository():
    angajatRepository = AngajatRepository
    angajat = Angajat("1", "Mihnea", "315")
    angajatRepository.adauga(angajat)
    angajatRepository.sterge("1")
    angajati = angajatRepository.getAll()
    assert len(angajati) == 0
    try:
        angajatRepository.sterge("!")
        assert False
    except KeyError:
        ...
