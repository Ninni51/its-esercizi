class Frazioni:
    numeratore:int
    denominatore:int

    def __init__(self, numeratore, denominatore) -> None:
        self._numeratore = numeratore
        self._denominatore = denominatore

    def setNum(self, numeratore) -> None:
        if numeratore % 1 == 0:
            self._numeratore = 13
        else:
            self._numeratore = numeratore
    
    def getNum(self) -> int:
        return self._numeratore
    
    def setDen(self, denominatore) -> None:
        if denominatore % 1 == 0 or denominatore == 0:
            self._denominatore = 5
        else:
            self._denominatore = denominatore
    
    def getDen(self) -> int:
        return self._denominatore
    
    def __str__(self):
        return "Numeratore = " + str(self._numeratore) + " / Denominatore = " + str(self._denominatore)

    @staticmethod
    def value(numeratore, denominatore) -> float:
        valore:float = numeratore/denominatore
        valore = round(valore, 3)
        return valore
    
    def mcd(x:int, y:int) -> int:
        divisore = 1
        if x > y:
            for i in range(2, y+1):
                if x%i == 0 and y%i == 0:
                    divisore = i
            return divisore
        elif x < y:
            for i in range(2, x+1):
                if x%i == 0 and y%i == 0:
                    divisore = i
            return divisore
        else: 
            divisore = x
            return divisore
        
    def semplifica(lista:list) -> list:
        r = []
        for fr in lista:
            num = Frazioni.getNum(fr)
            den = Frazioni.getDen(fr)
            div = Frazioni.mcd(num, den)
            if div == 1:
                r.append(str(fr))
            else:
                new_fr = Frazioni(num // div, den // div)
                r.append(str(new_fr))
        return r

    def fractionCompare(m:list) -> None:
            r = Frazioni.semplifica(m)
            for i, j in m:
                k = Frazioni.getNum(r)
                l = Frazioni.getDen(r)
                print(f"{Frazioni.value(i, j)} == {Frazioni.value(r)}")

Frazioni.semplifica([15, 5])