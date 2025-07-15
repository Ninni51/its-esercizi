import string
import os.path

class Documento:
    testo:str

    def __init__(self, testo):
        self.setText(testo)

    def setText(self, testo):
        self.testo = testo

    def getText(self):
        return self.testo
    
    def isInText(self, testo, parola):
        sep = self.testo.split()
        for i in range(0, len(sep)):
            if parola == sep[i].strip(string.punctuation):
                return True
        return False
    
class Email(Documento):
    def __init__(self, mittente, destinatario, titolo, testo):
        super().__init__(testo)
        self.setMittente(mittente)
        self.setDestinatario(destinatario)
        self.setTitolo(titolo)

    def getMittente(self):
        return self.mittente

    def setMittente(self, mittente):
        self.mittente = mittente

    def getDestinatario(self):
        return self.destinatario

    def setDestinatario(self, destinatario):
        self.destinatario = destinatario

    def getTitolo(self):
        return self.titolo

    def setTitolo(self, titolo):
        self.titolo = titolo

    def getText(self):
        return f"Da: {self.getMittente()}, A: {self.getDestinatario()}\nTitolo: {self.getTitolo()} \nMessaggio: {super().getText()}"

    def setText(self, testo):
        super().setText(testo)

    def writeToFile(self):
        filename = "email.txt"
        path = "Dell/Documenti"
        completepath = os.path.join(path, filename)
        content = self.getText()
        with open(completepath, "w") as file:
            file.write(content)
        
class File(Documento):
    nomepercorso:str
    
    def writeToFile(self):
        filename = "email.txt"
        path = "Dell/Documenti"
        completepath = os.path.join(path, filename)
        content = self.getText()
        with open(completepath, "w") as file:
            file.write(content)
    
class File(Documento):
    nomepercorso:str

    def __init__(self, nomepercorso):
        self.nomepercorso = nomepercorso
        self.testo = super().getText()
    
    def leggiTestoDaFile(self):
        file_path = os.path.join(self.nomepercorso, "document.txt")
        
        with open(file_path, "r", encoding="utf-8") as f:
            self.testo = f.read()
    
    def getText(self):
        # Ritorna la stringa formattata come richiesto
        return (f"Percorso: {os.path.join(self.nomepercorso, 'document.txt')}\n"
                f"Contenuto: {self.testo}")
