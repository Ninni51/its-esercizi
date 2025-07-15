import random

class Creatura:
    _nome: str

    def __init__(self, nome) -> None:
        self.setNome(nome) 

    def setNome(self, nome) -> None:
        if isinstance(nome, str) and nome != "":
            self._nome = nome
        else:
            self._nome = "Creatura Generica"

    def getNome(self) -> str:
        return self._nome

    def __str__(self) -> str:
        s = "Creatura: " + self._nome
        return s
    
class Alieno(Creatura):
    _matricola: int
    _munizioni: list

    def __init__(self) -> None:
        self.__setMatricola()
        self.__setMunizioni()
        self._nome = f"Robot-{self._matricola}"
#       Questo l'ho preso online perchè francamente non avevo idea di come farlo, ma allo stesso tempo, a meno che uno non edita manualmente gli attributi
#       Non dovrebbe essere neanche possibile che il nome del robot sia diverso da una certa matricola
#
#        if not self._nome.startswith("Robot-") or not self._nome[6:].isdigit():
#            print("Attenzione! Tutti gli Alieni devono avere il nome \"Robot\" seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!")
#            self._nome = f"Robot-{self._matricola}"

    def __setMatricola(self) -> None:
        self._matricola = random.randint(10000, 90000)

    def __setMunizioni(self) -> None:
        self._munizioni = [i**2 for i in range(15)]

    def getMatricola(self) -> int:
        return self._matricola

    def getMunizioni(self) -> list:
        return self._munizioni

    def getNome(self) -> str:
        return self._nome

    def __str__(self) -> str:
        return "Alieno: " + self._nome

class Mostro(Creatura):
    _urlo_vittoria: str
    _gemito_sconfitta: str
    _nome: str
    _assalto: list

    def __init__(self, nome:str, vittoria: str, sconfitta: str) -> None:
        self.__setVittoria(vittoria)
        self.__setSconfitta(sconfitta)
        self.setNome(nome)
        self.__setAssalto()

    def __setVittoria(self, urlo: str) -> None:
        if isinstance(urlo, str) and urlo != "":
            self._urlo_vittoria = urlo
        else:
            self._urlo_vittoria = "GRAAAHHH"

    def __setSconfitta(self, urlo: str) -> None:
        if isinstance(urlo, str) and urlo != "":
            self._gemito_sconfitta = urlo
        else:
            self._gemito_sconfitta = "Uuurghhh"

    def __setAssalto(self) -> list:
        self._assalto = []
        while len(self._assalto) != 15:
            n = random.randint(1, 101)
            if n not in self._assalto:
                self._assalto.append(n)
        return self._assalto

    def getVittoria(self) -> str:
        return self._urlo_vittoria

    def getSconfitta(self) -> str:
        return self._gemito_sconfitta

    def getAssalto(self) -> list:
        return self._assalto

    def __str__(self) -> str:
        nome = self.getNome()
        res = ''.join([nome[i].upper() if i % 2 == 0 else nome[i].lower() for i in range(len(nome))])
        return res
    
def PariUguali(a:list[int], b:list[int]) -> list[int]:
    c = []
    if len(a) == len(b):
        for i in range(len(a)):
            if a[i] % 2 == 0 and b[i] % 2 == 0:
                c.append(1)
            else:
                c.append(0)
    else:
        print("Errore! Lunghezza liste non equivalente")
    return c

def Combattimento(a:Alieno, m:Mostro) -> None:
    muni = a.getMunizioni()
    ass = m.getAssalto()
    if not a == isinstance(a, Alieno) and m == isinstance(m, Mostro):
        print("Un combattimento non può avvenire se non tra un mostro e un alieno")
        return None
    else:
        if sum(PariUguali(muni, ass)) > 4:
            proclamaVincitore(m)
        else:
            proclamaVincitore(a)

def proclamaVincitore(c: Creatura) -> None:
    contenuto = str(c)
    altezza = 5
    larghezza = len(contenuto) + 10
    for i in range(altezza):
        for j in range(larghezza):
            if i == 0 or i == altezza - 1:
                print("*", end="")
            elif j == 0 or j == larghezza - 1:
                print("*", end="")
            elif i == 2 and j == 5:
                print(c, end="    *")
                break
            else:
                print(" ", end="")
        print()
    
def main():
    mo = Mostro("Godzilla", "RAAWR!", "urghh...")
    al = Alieno()
    print("Dati Mostro:")
    print("Nome:", mo.getNome())
    print("Assalto:", mo.getAssalto())
    print()
    print("Dati Alieno:")
    print("Nome:", al.getNome())
    print("Munizioni:", al.getMunizioni())
    print()
    print("Combattono!")
    Combattimento(al, mo)

main()

