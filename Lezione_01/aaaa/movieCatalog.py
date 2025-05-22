class MovieCatalog:

    def __init__ (self) -> None:
        self.setCatalog()

    def __str__():

    
    def setCatalog(self) -> None:
        self.catalog: dict[str, list[str]] = {}
    
    def getCatalog(self) -> dict[str, list[str]]:
        return self.catalog
    
    def add(self, directorname:str, movies:str) -> None:
        if not directorname:
            print("Fornire un nome valido per il regista")
        elif not movies:
            print("Fornire un film valido")
        else:
            for movie in movies:
                if movie in self.catalog[directorname]:
                    pass
                else:
                    if directorname in self.catalog and movie in self.catalog[directorname]:
                        self.catalog[directorname].append(movies)
    
    def remove(self, directorname:str, movies:str) -> None:
        if not directorname:
            print("Fornire un nome valido per il regista")
        elif not movie:
            print("Fornire un film valido")
        else:
            if directorname in self.catalog and movie in self.catalog[directorname]:
                self.catalog[directorname].remove(movies)
            if not self.catalog[directorname]:
                del directorname

