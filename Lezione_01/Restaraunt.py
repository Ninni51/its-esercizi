class Restaraunt:
    def __init__(self, name, cuisineType, numberServed=0):
        self.name = name
        self.cuisineType = cuisineType
        self.numberServed = numberServed

    def describeRestaraunt(self) -> None:
        print(f"The restaurant's name is {self.name} and its cuisine type is {self.cuisineType}")

    def OpenRestaraunt(self) -> None:
        print(f"{self.name} is open")

    def setNumberServed(self, numberServed) -> None:
        self.numberServed = numberServed 
    
    def incrementNumberServed(self) -> None:
        self.numberServed = self.numberServed+int(input("Add the amount of clients that have been served today"))
'''
risto1 = Restaraunt("Giggio", "Pasta")
risto2 = Restaraunt("O' Masto", "Pizza")
risto3 = Restaraunt("Akira", "Ramen")

risto1.describeRestaraunt()
risto1.OpenRestaraunt()

risto2.describeRestaraunt()
risto3.describeRestaraunt()

risto1.setNumberServed(3)
print(risto1.numberServed)

risto1.incrementNumberServed()
'''