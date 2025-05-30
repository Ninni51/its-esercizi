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

    def increment_login_attempts(self) -> None:
        self.loginAttempts += 1  

    def reset_login_attempts(self) -> None:  
        self.loginAttempts = 0  

user1 = User("Mauro", "Abate", 53, "M")
user1.describeUser()
user1.greetUser()

print(f"Login attempts: {user1.loginAttempts}")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"Login after incrementing: {user1.loginAttempts}")
user1.reset_login_attempts()
print(f"Login reset: {user1.loginAttempts}")
