class User:
    def __init__(self, name: str, lastname: str, age: int, gender: str, loginAttempts: int = 0):  
        self.name = name
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.loginAttempts = loginAttempts  

    def describeUser(self) -> None:
        print(f"The user's name is {self.name}, the user's surname is {self.lastname}, the user's age is {self.age}, the user's gender is {self.gender}")

    def greetUser(self) -> None:
        if self.gender == "M":
            if self.age < 18:
                print(f"Hello, young mister {self.name}")  # Fixed space issue
            else:
                print(f"Hello sir {self.name}")
        elif self.gender == "F":
            if self.age < 18:
                print(f"Hello, young madam {self.name}")  # Fixed space issue
            else:
                print(f"Hello lady {self.name}")

class Privileges:
    def __init__ (self, canEdit:bool, canAccess:bool, canComment:bool, canDelete:bool):
        self.canEdit = canEdit
        self.canAccess = canAccess
        self.canComment = canComment
        self.canDelete = canDelete

    def showPrivileges(self) -> None:
        print(f"User privileges: \n Editing: {self.canEdit}\n Accessing: {self.canAccess}\n Commenting: {self.canComment}\n Deleting: {self.canDelete}")

class Admin:
    def __init__(self, user:User, privileges:Privileges):
        self.User = user
        self.Privileges = privileges

utente = User("Ciccio", "Pasticcio", 20, "M")
utentepermessi = Privileges(True, True, True, True)

User1 = Admin(utente, utentepermessi)
User1.utente.greetUser()
User1.utentepermessi.showPrivileges()