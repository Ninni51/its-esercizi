from persona import Persona

class Studente(Persona):

    '''
    Attributi della classe Persona
    self.name: str
    self.lastname: str
    self.age: int

    '''

def __init__(self, name:str, lastname:str, age:int, matricola:str):
    super().__init__(name, lastname, age)
    self.matricola(matricola)

def setMatricola(self, matricola) -> None:
    if matricola:
        self.matricola = matricola
    else:
        print("Errore, la matricola è vuota")

def getMatricola(self) -> str:
    return self.matricola

def __str__(self) -> str:
    return f"\nNome: {self.name}\nCognome: {self.cognome}\nEtà: {self.age}"
    