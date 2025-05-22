
def sorter(l: list) -> None:
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            placeholder = l[i + 1]
            l[i + 1] = l[i]
            l[i] = placeholder

def bubbleSort(lista: list) -> list:
    n = len(lista)
    for i in range(n):
        sorter(lista)
    return lista

print(bubbleSort([1, 4, 7, 3, 2, 1, 3, 5, 8, 9, 10, 11, 13]))
