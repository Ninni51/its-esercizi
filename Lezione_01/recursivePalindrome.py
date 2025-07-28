import math

def recursivePalindrome(word:str, i:int = 0, j:int = -1, count = 0) -> bool:
    if count == 0:
        word = word.replace(" ", "")
        word = word.lower()
    if len(word)%2 == 0:
        if count == len(word)/2:
            return True
    else:
        if count == math.floor(len(word))+1:
            return True
    if word[i] == word[j]:
        i+=1
        j-=1
        count+=1
        return recursivePalindrome(word, i, j, count)
    else:
        return False

print(recursivePalindrome("anna"))
    
def uniqueNames() -> None:
    lista = []
    lungo = ""
    fl = True
    while fl == True:
        nome = input("Inserisci un Nome:")
        if nome not in lista:
            lista.append(nome)
            if len(lungo) < len(nome):
                lungo = nome
        else:
            fl = False
    print(f"Hai inserito {len(lista)} nomi diversi.")
    print(f"Il nome più lungo inserito è {lungo} con {len(lungo)} Caratteri")

uniqueNames()