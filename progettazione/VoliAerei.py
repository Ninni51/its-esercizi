from typing import Self
from custom_types import IntGE1900, IntGT0, IntGE0

class Codice(str):
    def __new__(cls, c: str) -> Self:
        c = c.strip().upper()
        if not c:
            raise ValueError("Il codice non può essere vuoto!")
        return super().__new__(cls, c)

class Nome(str):
    def __new__(cls, n: str) -> Self:
        if not n:
            raise ValueError("Il nome non può essere vuoto!")
        return super().__new__(cls, n)

class Volo:
    _codice: Codice
    _durata: IntGT0

    def codice(self) -> Codice:
        return self._codice

    def durata_minuti(self) -> IntGT0:
        return self._durata

    def __init__(self, codice: str, durata_minuti: int) -> None:
        self._codice = Codice(codice)
        self._durata = IntGT0(durata_minuti)

    def __repr__(self) -> str:
        return f"Volo {self.codice()}, durata {self.durata_minuti()} minuti"

class Compagnia:
    _nome: Nome
    _fondazione: IntGE1900

    def nome(self) -> Nome:
        return self._nome

    def fondazione(self) -> int:
        return self._fondazione
    
    def __init__(self, nome: str, fondazione: int) -> None:
        self._nome = Nome(nome)
        self._fondazione = IntGE1900(fondazione)

    def __repr__(self) -> str:
        return f"Compagnia {self.nome()} (fondata nel {self.fondazione()})"

class Città:
    _nome: Nome
    _n_abitanti: IntGE0

    def nome(self) -> Nome:
        return self._nome

    def abitanti(self) -> int:
        return self._n_abitanti
    
    def __init__(self, nome: str, n_abitanti: int) -> None:
        self._nome = Nome(nome)
        self._n_abitanti = IntGE0(n_abitanti)

    def __repr__(self) -> str:
        return f"Città di {self.nome()} con {self.abitanti()} abitanti"

class Nazione:
    _nome: Nome

    def __init__(self, nome: str) -> None:
        self._nome = Nome(nome)

    def nome(self) -> Nome:
        return self._nome

    def __repr__(self) -> str:
        return f"Nazione {self.nome()}"

class Aeroporto:
    pass