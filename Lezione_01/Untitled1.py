
n = int(input("Inserire il numero di volte che deve runnare il programma."))
while n%1!=0:
    print("Errore, numero di volte invalido inserito")
    n = int(input("Inserire il numero di volte che deve runnare il programma."))

i = 1
somma = 0
media = 0
somma_pari = 0
somma_dispari = 0

while i != n+1:
    x = int(input("Inserire un numero."))
    while x%1!=0:
        print("Errore, numero invalido inserito")
        x = int(input("Inserire un numero."))
    somma+=x
    media = somma/i
    if x%2 == 0 and x>media:
        somma_pari+=x
    else:
        somma_dispari +=x
    i+=1

print(f"La somma dei pari è {somma_pari}")
print(f"La somma dei dispari è {somma_dispari}")

if somma_pari>somma_dispari:
    print("Somma pari > Somma dispari")
elif somma_dispari>somma_pari:
    print("Somma dispari>Somma Pari")
else:
    print("Somme uguali")