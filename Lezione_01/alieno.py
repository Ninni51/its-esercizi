class Alieno:

    def __init__(self, galaxy:str):
        self.setGalaxy(galaxy)
    
    def setGalaxy(self, galaxy:str):
        if galaxy:
            self.galaxy = galaxy
        else:
            print("Errore, la galassia non può essere una stringa vuota!")
        