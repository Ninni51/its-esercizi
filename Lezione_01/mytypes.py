class Persona (object): 

    nome: str = "a"

    def __new__(cls, *args, **kwargs) -> self: 
        return super().__new__(cls)

    def __init__(self, nome:str) -> None:
        self.nome = nome
    
    def __eq__(self, other:Any) -> bool:
        if not isinstance(other, Persona):
            return False
        return self.nome == other.nome
    
    
    def __repr__(self) -> str:
        return f'Persona ({self.cf} e nome {self.nome})'
    
class Voto(int):
    def __new__(self, int) -> None:
    pass

from typing import Self, Any
from enum import *
class Genere (StrEnum):
    Uomo = auto()
    donna = auto()
class Continente (StrEnum): 
    asia = auto()
    europa = auto()
    america= auto()
    africa = auto() 
    antartide = auto()
    
if __name__ == '__main__': 
    print (Genere.uomo.upper()) 
    print(type (Genere.donna))
    print(Continente.america.capitalize())

if __name__ == '__main__':
    alice1: Persona = Persona("Alice")
    print (type(alice1))
    print("Superclasse di Persona: " +str(Persona.mro()[-1]))

    alice2: Persona = Persona("Alice")

