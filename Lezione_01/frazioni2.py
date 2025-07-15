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

    def value(self) -> float:
