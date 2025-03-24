class Restaraunt:
    def __init__(self, name, cuisineType):
        self.name = name
        self.cuisineType = cuisineType
    
    def describeRestaraunt(self) -> None:
        print(f"The restaraunt's name is {self.name} and its cuisine type is {self.cuisineType}")
    
    def OpenRestaraunt(self) -> None:
        print(f"{self.name} is open")
    
risto1 = Restaraunt("Giggio", "Pasta")
risto2 = Restaraunt("O' Masto", "Pizza")
risto3 = Restaraunt("Akira", "Ramen")

risto1.describeRestaraunt()
risto1.OpenRestaraunt()

risto2.describeRestaraunt()
risto3.describeRestaraunt()