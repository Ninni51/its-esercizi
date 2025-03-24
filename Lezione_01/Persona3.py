class Person:
    personCount = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.personCount += 1

    def displayData(self) -> None:
        print(f"Nome: {self.name}\n Età: {self.age}")

alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)

bob.displayData()

if bob.age > alice.age:
    bob.displayData()
else:
    alice.displayData()

tarko = Person("Tarko V.", 65)
marko = Person("Mark O.", 3)
barko = Person("Barko D.", 112)
people = [alice, bob, tarko, marko, barko]

for i in people:
    if i.age == people[0].age:
        youngest = i
    else:
        if i.age < youngest.age:
            youngest = i    

youngest.displayData()