import math

def calculateCharges(charges:list) -> list:
    tab = [["Cars", "Hours", "Charge"]]
    rows:int = len(charges)
    columns:int = 3
    charge:float
    total:float = 0
    totalcharge:float = 0
    for i in range(len(charges)):
        hours = float(charges[i])
        if hours < 0 or hours > 24:
            raise ValueError("Hours must be between 0 and 24.")
        if hours < 3:
            charge = 2.00
        elif hours == 24:
            charge = 10.00
        else:
            charge = 2.00 + ((math.ceil(hours) - 3) * 0.50)
        total += hours
        totalcharge += charge
        row = [i + 1, hours, charge]
        tab.append(row)
    for col in tab[0]:
        print(col, end="    ")
    print()
    for i in range(1, rows):
        for j in range(columns):
            print(f"{tab[i][j]}", end="       ")
        print("$")
    print(f"TOTAL   {total}      {totalcharge}      $")

calculateCharges([5, 5.5, 4.4, 3.0, 9])

def printListBackwards(l:list, val:int = -1):
    print(l[val])
    if len(l)+val == 0:
        print("Done!")
    else:
        printListBackwards(l, val-1)

printListBackwards([0, 1, 2, 3, 4, 5, 6])