from custom_types import Indirizzo

class Dipartimento:
    _nome: str
    _telefoni: set[str]
    _indirizzo: Indirizzo
    _città: str

    def __init__(self, nome:str, telefono:str, Indirizzo:Indirizzo):
        self.set_nome(nome)
        self.set_telefono(telefono)
        self.set_indirizzo(Indirizzo)

    def nome(self) -> str:
        return self._nome

    def set_nome(self, nome) -> None:
        self._nome = nome

    def set_città(self, città) -> None:
        self._città = città

    def telefoni(self) -> set[str]:
        return self._telefoni

    def add_telefono(self, new_telefono) -> None:
        self._telefoni.add(new_telefono)

    def remove_telefono(self, t:str) -> None:
        if len(self.telefoni()) > 1:
            self._telefoni.remove(t)
        raise RuntimeError('Il dipartimento deve avere almeno un numero di telefono')
    
    def Indirizzo(self, Indirizzo) -> Indirizzo:
        return self._indirizzo 
    
    def set_indirizzo(self, Indirizzo) -> None:
        Indirizzo = self.Indirizzo