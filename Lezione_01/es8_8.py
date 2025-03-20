
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