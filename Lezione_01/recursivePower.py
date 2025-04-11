
def recursivePower(base:int, exponent:int, result = 0, initialexponent = 0) -> None:
    if result == 0:
        result = base
        initialexponent = exponent
    if exponent > 1:
        result = result*base
        exponent -= 1
        recursivePower(base, exponent, result, initialexponent)
    else:
        print(f"{base} to the power of {initialexponent} is {result}")

recursivePower(3, 4)
recursivePower(4, 3)
recursivePower(2, 5)
recursivePower(5, 2)