class Animal:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs
    def getLegs(self, legs:str) -> str:
        return self.legs
    def setLegs(self, legs:int) -> int:
        self.legs = legs
        return self.legs
    def printInfo(self) -> None:
        print(f"Name: {self.name}\n Legs: {self.legs}")

dog = Animal("Dog", 4)
millipede = Animal("Millipede", 1000)

print(f"{dog.name}")

dog.legs = 7

print(f"{dog.legs}")

dog.setLegs(10)

print(f"{dog.legs}")

print(millipede.getLegs(millipede))

dog.printInfo()