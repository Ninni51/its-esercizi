from custom_types import *
from datetime import date

class Impiegato:
    _nome: str
    _cognome:str
    _nascita:date
    _stipendio: RealGEZ

    def nome(self) -> str:
        return self._nome
    
    def cognome(self) -> str:
        return self._cognome
    
    def nascita(self) -> date:
        return self._nascita
    
    def stipendio(self) -> RealGEZ:
        return self._stipendio
    
    def set_nome(self, nome) -> None:
        self._nome = nome

    def set_cognome(self, cognome) -> None:
        self._cognome = cognome

    def set_stipendio(self, stipendio) -> None:
        self._stipendio = stipendio

    def __init__(self, nome:str, cognome:str, nascita:date, stipendio:RealGEZ) -> None:
        self.set_nome(nome)
        self.set_cognome(cognome)
        self.set_stipendio(stipendio)

    def __str__ (self) -> str:
        return f"{self.nome()} {self.cognome}, nascitas: {self.nascita()}, stipendio {self.stipendio()}"