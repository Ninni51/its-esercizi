
def conversione(t: list[tuple]) -> dict:
    convertito = {}
    for i, j in t:
        if i in convertito:
            convertito[i] += j
        else:
            convertito[i] = j
    return convertito

print(conversione([("quattro", 4), ("tre", 3), ("due", 2), ("uno", 1), ("zero", 0), ("uno", 3)]))

def separazione(t: list) -> dict:
    liste = {"positivi":[], "negativi":[]}
    for i in t:
        if i >= 0:
            liste["positivi"].append(i)
        else:
            liste["negativi"].append(i)
    return liste

print(separazione([0, 2, -3, 5, -8, 4, 3]))

def negozio(d:dict) -> dict:
    newd = {}
    for k, v in d.items():
        if v > 50:
            continue
        else:
            newd[k]= round((v*110/100),2)
    return newd

print(negozio({"mela":40, "mazzo":20, "pazzo":80, "razzo":10}))

def check(x:bool, y:bool, z:bool) -> str:
    azione = "Azione Permessa"
    if x != True:
        azione = "Azione Negata"
    if y != True and z != True:
        azione = "Azione Negata"
    return azione

print(check(True, True, False))

def thresh(t:list[int], threshold: int) -> int:
    sum = 0
    for i in t:
        if i < threshold:
            if sum == 0:
                sum = i
            else:
                sum = sum*i
    return sum

for i in range(0, 15, 2):
    print(i)

for i in range(1, 14, 3):
    print(i)

for i in range(30, -1, -5):
    print(i)

for i in range(5, 50, 10):
    print(i)