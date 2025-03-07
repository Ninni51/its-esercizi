
x = int(input("Inserire un numero."))
if x%1!=0 and x<0:
    print("Errore, numero invalido inserito")
else:
    if x%2==0:
        valore=0
        numero=4
        while numero<=x:
            valore+=numero
            numero+=4
        print(f"La somma è {valore}")
    else:
        valore=1
        numero=1
        while numero <=x:
            numero=numero*valore
            numero+=2
        print(f"Il prodotto è {valore}")
    

