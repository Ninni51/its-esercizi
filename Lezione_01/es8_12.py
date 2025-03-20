
def sandwich(**kwargs) -> list:
    print(f"So, you want a sandwich with {fillings}, correct?")

fillings = {'keyword1': "Dayum",'keyword2': "Goddamn", 'keyword3': "Onion", 'keyword4':"Sauce"}
print(sandwich(**fillings.values()))