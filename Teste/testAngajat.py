from domain.angajat import Angajat


def testAngajat():
    angajat = Angajat("1", "Ana", "231")
    assert angajat.getIdAngajat() == "1"
    assert angajat.getNume() == "Ana"
    assert angajat.getCNP() == "231"

def testsetteri():
    angajat = Angajat("2", "Marcel", "132")
    angajat.setIdAngajat("3")
    assert angajat.getIdAngajat() == "3"

    angajat.setNume("Paul")
    assert angajat.getNume() == "Paul"

    angajat.setCNP("510")
    assert angajat.getCNP() == "510"
