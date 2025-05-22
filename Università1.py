from datetime import date

class Corso:
    def __init__(self, nome: str, crediti_formativi: int, anno_accademico: date):
        if crediti_formativi < 0:
            raise ValueError("Uno studente non può avere crediti formativi negativi.")
        self.nome = nome
        self.crediti_formativi = crediti_formativi
        self.anno_accademico = anno_accademico

class Esercitazione:
    def __init__(self, codice: str):
        if not (len(codice) == 16 and codice.isalnum()):
            raise ValueError("Il codice deve essere una stringa alfanumerica di esattamente 16 caratteri.")
        self.codice = codice

class Esercizio:
    def __init__(self, testo: str, soluzione: str):
        self.testo = testo
        self.soluzione = soluzione

class Docente:
    def __init__(self, name: str):
        self.name = name