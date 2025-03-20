class Persona:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def displayData(self) -> None:
        print(f"Nome: {self.name}\n Cognome: {self.lastname}\n Età: {self.age}")
    
    def setName(self, name:str) -> None:
        self.name = name

    def setLastName(self, lastname:str) -> None:
        self.lastname = lastname
        
    def setAge(self, age:str) -> None:
        if age < 0 or age > 130:
            self.age = 0
        else:
           self.age = age

    def getName(self, name:str) -> str:
        return self.name

    def setLastName(self, lastname:str) -> str:
        return self.lastname
        
    def setAge(self, age:str) -> int:
        if age < 0 or age > 130:
            return self.age = 0
        else:
            return self.age

fm:Persona = Persona()

fm.displayData()

fm.setName("Nicholas")

fm.setLastName("Marsella")

fm.setAge("22")

fm.displayData()
