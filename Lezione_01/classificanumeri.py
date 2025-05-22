def classifica_numeri(lista: int) -> dict[str:list[int]]:
    dict = {"pari": [], "dispari": []}
    for i in lista:
        if lista[i] % 2 == 0:
            dict["pari"].append(i)
        else:
            dict["dispari"].append(i)
    return dict

def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
    dict = {}
    for i, j in tuples:
        if i not in dict:
            dict[i] = []
        dict[i].append(j)
    return dict

def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    for i in lista:
        while da_rimuovere[1] > 0:
            if i == da_rimuovere[0]:
                lista.remove[i]
                da_rimuovere[1] = da_rimuovere[1]-1
    return lista

def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int, int]) -> list[int]:
    for v, q in da_rimuovere.items():
        while q > 0 and v in lista:
            lista.remove(v)
            q -= 1
    return lista

def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    voti_agg = {}
    for i in voti:
        n = i['nome']
        v = i['voto']        
        if n not in voti_agg:
            voti_agg[n] = []
        voti_agg[n].append(v)
    return voti_agg

def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    for prodotto, prezzo in prodotti.copy().items():
        print(prodotto)
        if 20 < prezzo:
            prezzoscontato = prezzo*9/10
            prodotti[prodotto] = prezzoscontato
        else:
            prodotti.pop(prodotto)
    return prodotti

def create_contact(name: str, email: str=None, telefono: int=None) -> dict:
    contact = {"profile": name, "email": email, "telefono": telefono}
    return contact

def update_contact(contact:dict, name: str = None, email: str=None, telefono: int=None) -> dict:
    updated_contact = contact
    if name != None:
        updated_contact["profile"] = name
    if email != None:
        updated_contact["email"] = email
    if name != None:
        updated_contact["telefono"] = telefono
    return updated_contact

contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
print(contact)

print(update_contact(contact, "Mario Rossi", telefono=123456789))

