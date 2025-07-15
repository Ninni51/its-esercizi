import random

def genera(dim:int) -> list[list[int]]:
    mat: list[list[int]] = []
    for r in range(dim): 
        row: list[int] = []
        for c in range(dim):
                x = random.randint(0, 13)
                if c != 0:
                    while x == row[0]:
                        x = random.randint(0, 13)
                row.append(x)
        mat.append(row)
    return mat

def printMAT(mat: list[list[int]]) -> None:
    for r in range(len(mat)):
        for c in range(len(mat[r])):
            print(f"{mat[r][c]:<5}", end="")
        print("\n")

def calcolaCarico(mat: list[list[int]], riga: int, colonna: int) -> int:
    somma_riga = sum(mat[riga])
    somma_colonna = sum(row[colonna] for row in mat)
    carico = somma_riga - somma_colonna
    return carico

def caricoNullo(mat:list[list[int]]) -> list:
    nulli = []
    for r in range(len(mat)):
        for c in range(len(mat[r])):
            carico = calcolaCarico(mat, r, c)
            if carico == 0:
                nulli.append((r+1, c+1))
    return nulli

def caricoMax(mat:list[list[int]]) -> list:
    for r in range(len(mat)):
        for c in range(len(mat[r])):
            if r == 0 and c == 0:
                carico = calcolaCarico(mat, r, c)
                max = carico
                maxpos = (r, c)
            else:
                carico = calcolaCarico(mat, r, c)
                if carico > max:
                    max = carico
                    maxpos = (r, c)
    return maxpos

def caricoMin(mat:list[list[int]]) -> list:
    for r in range(len(mat)):
        for c in range(len(mat[r])):
            if r == 0 and c == 0:
                carico = calcolaCarico(mat, r, c)
                min = carico
                minpos = (r, c)
            else:
                carico = calcolaCarico(mat, r, c)
                if carico < min:
                    min = carico
                    minpos = (r, c)
    return minpos

x = genera(5)
printMAT(x)
print(f"Nulli: {caricoNullo(x)}")
print(f"Massimo: {caricoMax(x)}")
print(f"Min: {caricoMin(x)}")
print(f"{calcolaCarico(x, caricoMax(x))}")
print(f"{calcolaCarico(x, caricoMin(x))}")

