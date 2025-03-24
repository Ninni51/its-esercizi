class User:
    def __init__(self, name:str, lastname:str, age:int, gender:str):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.gender = gender
    def describeUser(self) -> None:
        print(f"The user's name is {self.name}, the user's surname is {self.lastname}, the user's age is {self.age}, the user's gender is {self.gender}")
    def greetUser(self) -> None:
        if self.gender == "M":
            if self.age < 18:
                print("Hello, young mister")