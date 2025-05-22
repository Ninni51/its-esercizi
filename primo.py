
def prime(num:int) -> bool:
    primo = True
    for i in range (2, num):
        if num % i == 0:
            primo = False
        if primo == False:
            break
    return primo

prime(14)