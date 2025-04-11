import math
def safe_sqrt(number) -> float:
    try:
        squareroot = math.sqrt(number)
    except ValueError as error:
        print("The inserted number is negative.")
    finally:
        return squareroot

class InvalidPasswordError(Exception):
    """Invalid Password"""

def validate_password(password) -> bool:
    valid = True
    upperCounter = 0
    specialCounter = 0
    if len(password) > 20:
        raise InvalidPasswordError("The password is too long.")
    for char in password:
        if char.isupper():
            upperCounter += 1
        if char.isalnum() != True:
            specialCounter += 1
    if upperCounter < 3:
        raise InvalidPasswordError("The password doesn't have enough uppercase letters.")
    if specialCounter <4:
        raise InvalidPasswordError("The password doesn't have enough special characters.")
    return valid

print(validate_password("__xXN1ck3rG4m3rsXx__"))
print(validate_password("ciao"))
        



