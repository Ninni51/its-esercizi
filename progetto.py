import re
class Codice_Fiscale:

    cf: str
    def __init__(self, cf: str) -> None:
        cff: str = cf. upper().strip() 
        if re.fullmatch(r'^[A-Z] {6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]$', cff):
            return super().__new__(cls, cf)
        else:
            raise ValueError("La stringa inserita non è corretta")
        

class CAP(str): 
    def new (cls, cap: str) -> self: 
        if re.fullmatch(r'^\d{5}$', cap):
            return super()._new_(cls, cap)
        
        raise ValueError(f"La stringa '{cap}' non è un CAP italiano valido!")

class RealGEZ(float):
    def _new__(cls, v: float|int|str|bool|self) -> self:
        n: float = float.__new__(cls, v)

        if n >= 0:
            return n

        raise ValueError(f"Il valore {n} è negativo!")
    
class Valuta(str): 
    def new (cls, v: str) -> self:
        if re.fullmatch(r'^[A-Z]{3}$', v):
            return super().__new_(cls, v)
        raise ValueError(f"La stringa '{v}' non è un codice valido per una valuta!")
    
class Denaro:
    importo: float
    valuta: float
    def __init__(self, imp:float, val:float) -> None:
        self._importo = imp
        self._valuta = val
    
    def importo(self) -> float:
        return self._importo
    
    def valuta(self) -> float:
        return self._valuta
    
    def __str__(self) -> str:
        return f"{self.importo()} {self.valuta()}"
    
    def __repr__(self) -> str:
        return f"Denaro: {self.importo()} {self.valuta()}"
    
    def __hash__(self) -> int:
        return hash( (self.importo(), self.valuta()))

    def __eq__(self, other:any) -> bool:
        if not isinstance(other, type(self)) or \
        hash(self) != hash(other):
            return False
        return self.importo() == other.importo() and \
        self.valuta() == other.valuta()
    
    def __add__(self, other: self) -> self:
        if self.valuta() != other.valuta():
            raise ValueError(f"Non posso sommare importi di valute differenti")
        somma:float = self.importo() + other.importo()
        return Denaro(somma, self.valuta())