from Repository.AngajatRepository import AngajatRepository
from Service.AngajatService import AngajatService
from Teste.TestALL import testALL
from UI.Console import Consola


def main():
    #testALL()

    angajatRepository = AngajatRepository()
    angajatService = AngajatService(angajatRepository)
    consola = Consola(angajatService)

    consola.meniu()

main()