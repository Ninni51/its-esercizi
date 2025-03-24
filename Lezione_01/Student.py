class Student:
    def __init__(self, name:str, studyProgram:str, age:int, gender:str):
        self.name = name
        self.studyProgram = studyProgram
        self.age = age
        self.gender = gender
    
    def printInfo(self) -> None:
        print(f"Name: {self.name}\n Study Program: {self.studyProgram} \n Age: {self.age} \n Gender: {self.gender}")

Studente1 = Student("Nicholas", "Coding", 22, "M")
Studente2 = Student("Luca", "Fullstack", 20, "M")
Studente3 = Student("Gino", "Screzio", 26, "Elicottero")

Studente1.printInfo()
Studente2.printInfo()
Studente3.printInfo()
