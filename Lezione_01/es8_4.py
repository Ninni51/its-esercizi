
def make_shirt(size:str, message:str) -> None:
    print(f"The shirt is a size {size} and has {message} written on it.")

make_shirt("xl", "pipo pipo")

make_shirt(size="xl", message="pipo pipo")

def make_shirt(size:str = "large", message:str = "I love Python") -> None:
    print(f"The shirt is a size {size} and has {message} written on it.")

make_shirt()
make_shirt("Medium")
make_shirt(message = "pipo pipo")