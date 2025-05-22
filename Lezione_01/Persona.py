class Persona:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def displayData(self) -> None:
        print(f"Nome: {self.name}\n Cognome: {self.lastname}\n Età: {self.age}")
    
    def setName(self, name:str) -> None:
        if name:
            self.name = name
        else:
            print("Errore, non può essere una stringa vuota")

    def setLastName(self, lastname:str) -> None:
        if lastname:
            self.lastname = lastname
        else:
            print("Errore, non può essere una stringa vuota")

        
    def setAge(self, age:int) -> None:
        if age < 0 or age > 130:
            self.age = 0
        else:
           self.age = age

    def getName(self, name:str) -> str:
        return self.name

    def setLastName(self, lastname:str) -> str:
        return self.lastname
        
    def setAge(self, age:int) -> int:
        if age < 0 or age > 130:
            return self.age
        else:
            return self.age

fm:Persona = Persona("Nicholas", "Marsella", 22)

fm.displayData()

fm.setName("Nicholas")

fm.setLastName("Marsella")

fm.setAge(22)

fm.displayData()
