class Persona:
    '''

    Di una persona dobbiamo sapere le seguenti informazioni.
    Queste informazioni vengono chiamati attributi (della classe Persona)
    Le informazioni saranno:
    -nome
    -cognome
    -età
    self.name:str
    self.lastname:str
    self.age:int
    '''

    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age
    
    def displayData(self) -> None:
        print(f"Nome: {self.name}\n Cognome: {self.lastname}\n Età: {self.age}")
        
fm = Persona("Federico", "March", 29)

print(fm)

fm.displayData()