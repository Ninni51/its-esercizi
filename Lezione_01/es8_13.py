import send_messages()

def build_profile(firstname:str, lastname:str, age:int, haircolor:str, height:int) -> str:
    return(f"Name: {firstname}, Surname: {lastname}, Age {age}, {haircolor} hair, {height}cm tall")

print(build_profile("Nicholas", "Marsella", "22", "Brown", "165"))

