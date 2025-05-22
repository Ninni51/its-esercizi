import mathplotlib.pyplot as plt

def funz(num:int) -> int:
    if num % 2 == 0:
        num = num/2
    else:
        num = num*3+1
    return num

def Collatz(num: int) -> int:
    if num < 1 or num % 1 != 0:
        print("Il numero inserito non è valido.")
        num = 1
    while num != 1:
        num = int(funz(num))
        print(num)
    return num

print(Collatz(22.3))
    