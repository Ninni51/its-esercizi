import math
from typing import Callable
from functools import reduce


sqrt:Callable[[float], float] = lambda a: math.sqrt(a)
print(sqrt(4))

sum:Callable[[float, float], float] = lambda a, b: a+b
print(sum(4, 5))

numeri = [5, 12, 17, 18, 24, 32]
pari = list(filter(lambda x: x % 2 == 0, numeri))
print(pari)

studenti = [("Luca", 21), ("Anna", 19), ("Marco", 22)]
stud_ord = list(sorted(studenti, key=lambda student: student[1]))
print(stud_ord)

pari:Callable[[float], float] = lambda a: "Dispari" if a % 2 == 0 else "Dispari"
print(pari(5))

numeri = [2,3,4]
print(reduce(lambda a, b: a * b, numeri))

parole = ["cane", "gatto", "elefante", "ratto", "orso"]
shorter_than_5:list[str] = list(filter(lambda x: len(x) < 5, parole))
print(shorter_than_5)

studenti = [
    {"nome": "Anna", "media": 28},
    {"nome": "Luca", "media": 25},
    {"nome": "Marco", "media": 30}
]

media_ord = sorted(studenti, key=lambda student: student["media"])
print(media_ord)

from typing import Callable

def moltiplicatore(mult:int) -> Callable[[int], int]:
    fun = lambda x: x * mult
    return fun

per_due = moltiplicatore(2)
print(per_due(10))
