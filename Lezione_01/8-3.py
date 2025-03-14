
def display_message(message:str = "Stiamo imparando come definire e richiamare le funzioni contententi degli args.") -> None:
    print(message)

display_message()
display_message("pipo pipo")

def favorite_book(title:str) -> None:
    print(f"One of my favorite books is {title}.")

favorite_book("uhhhhhhhhh")

def make_shirt(size:str, message:str) -> None:
    print(f"The shirt is a size {size} and has {message} written on it.")

make_shirt("xl", "pipo pipo")

make_shirt(size="xl", message="pipo pipo")

def make_shirt(size:str = "large", message:str = "I love Python") -> None:
    print(f"The shirt is a size {size} and has {message} written on it.")

make_shirt()
make_shirt("Medium")
make_shirt(message = "pipo pipo")

def describe_city(city:str, country:str = "Italy") -> None:
    print(f"{city} is in {country}.")

describe_city("Rome")
describe_city("Milan")
describe_city("Tokyo", "Japan")

def city_country(city:str, country:str) -> str:
    return city, country

print(city_country("Tokyo", "Japan"))
print(city_country(f"Rome", "Italy"))
print(city_country(f"Santiago", "Chile"))

def make_album(artist:str, title:str, songs:None) -> dict:
    album = [artist, title, songs]
    return album

album1=make_album("Instalok", "Duo queue", None)
album2=make_album("Falconshield", "This is war", 7)
album3=make_album("Caleb Hyles", "In one Breath", None)

print(album1, album2, album3)

i = "Y"
while i != "N":
    albumartist = input()
    albumtitle = input()
    print(make_album(albumartist, albumtitle, None))
    i = input("Do you wish to continue? Y/N")
