from persona import Persona
from studente import Studente

am: Persona = Persona("Nicholas", "Marsella", 22)

print(am)

studente1: Studente = Studente("Mario", "Rossi", 20, "ASosa")

print(studente1)

if isinstance(studente1, Studente):
    print("\nstudente1 è un istanza della classe Studente")

if isinstance(am, Persona):
    print("\fam è un istanza della classe Persona")

if isinstance(am, Studente):
    print("am è oggetto della classe Persona e della classe Studente")
else:
    print("am è oggetto della classe Persona, ma non della classe studente")

# controllare che la classe Studente sia sottoclasse della classe Persona
# issubclass (Class1, Class2) -> controlla se Class1 sia sottoclasse della classe Class2 # in caso affermativo -> True
# in caso negativo -> False

if issubclass(Studente, Persona):
    print("Studente è sottoclasse della classe Persona")