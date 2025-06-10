
class Movie():
    def __init__(self, movie_id:str, title:str, director:str, is_rented:bool = False) -> None:
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = is_rented

    def get_title(self) -> str:
        return self.title

    def set_title(self, title: str) -> None:
        self.title = title


    def get_is_rented(self) -> bool:
        return self._is_rented

    def set_is_rented(self, is_rented: bool) -> None:
        self.is_rented = is_rented

    def rent(self, movie_title) -> None:
        if self.is_rented == True:
            print(f"Il film {movie_title} è già stato noleggiato")
        else:
            self.is_rented = True
    
    def return_movie(self, movie_title) -> None:
        if self.is_rented == False:
            print(f"Il film {movie_title} non è stato noleggiato da questo cliente.")
        else:
            self.is_rented = False
    
class Customer():
    def __init__(self, customer_id:str, name:str, rented_movies:list[Movie]) -> None:
        self.customer_id = customer_id
        self.name = name
        self.rented_movies = rented_movies
    
    def set_rented_movies(self, rented_movies):
        self.rented_movies = rented_movies

    def get_rented_movies(self):
        return self.rented_movies
    
    def rent_movie(self, movie:Movie) -> None:
        if Movie.get_is_rented(movie) == False:
            self.rented_movies.append(movie)
            Movie.rent(movie)
        else:
            print(f"Il film {movie.get_title()} è già stato noleggiato.")
    
    def return_movie(self, movie:Movie) -> None:
        if Movie.get_is_rented(movie) == True:
            self.rented_movies.remove(movie)
            Movie.return_movie(movie)
        else:
            print(f"Il film {movie.get_title()} non è stato noleggiato da questo cliente.")
    
class VideoRentalStore():
    def __init__(self, movies:dict[str, Movie], customers:dict[str, Customer]):
        self.movies = movies
        self.customers = customers
    
    def add_movie(self, movie_id:str, title:str, director:str):
        return Movie(movie_id, title, director)
    
    def register_customer(self, customer_id:str, name:str):
        return Customer(customer_id, name)
    
    def rent_movie(self, customer_id:str, movie_id:str):
        if customer_id and movie_id:
            Movie.rent()
            Customer.rent_movie()
    
    def return_movie(self, customer_id:str, movie_id:str):
        if customer_id and movie_id:
            Movie.return_movie()
            Customer.return_movie()
    
    def get_rented_movies(self, customer_id:str) -> list[Movie]:
        return Customer.get_rented_movies()

        