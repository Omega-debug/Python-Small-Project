from Teste.TestAngajatService import TestAdaugaAngajatService, TestStergeAngajatService, TestModificaAngajatService
from Teste.testAngajat import testAngajat, testsetteri
from Teste.testAngajatRepository import testAdaugaAngajatRepository, testStergeAngajatRepository, \
    testModificaAngajatRepository


def testALL():
    testAngajat()
    testsetteri()

    testAdaugaAngajatRepository()
    testStergeAngajatRepository()
    testModificaAngajatRepository()

    TestAdaugaAngajatService()
    TestStergeAngajatService()
    TestModificaAngajatService()

