# print("Sequenza a):")
# for i in range (1,8):
#     print(i)

# print("Sequenza b):")
# for i in range (3, 24, 5):
#     print(i)

# print("Sequenza c):")
# for i in range (20, -11, -6):
#     print(i) 
    
# print("Sequenza d):")
# for i in range (19, 52, 8):
#     print(i)

# def list_statistics(numbers: list[int]) -> (int, int, float):
#     for i in range(len(numbers)):
#         if i == 0:
#             max = numbers[i]
#             min = numbers[i]
#             sum = numbers[i]
#         else:
#             if numbers[i]>max:
#                 max=numbers[i]
#             if numbers[i]<min:
#                 min=numbers[i]
#             sum = sum+numbers[i]
#     avg = sum/len(numbers)
#     return max, min, avg
#
# print(list_statistics([1, 2, 3, 4, 5]))

def seconds_since_noon(hours:int, minutes:int, seconds:int) -> int:
    hours = hours%12
    minutes = minutes % 60
    seconds = seconds % 60
    while hours>0:
        seconds = seconds+3600
        hours-=1
    
    while minutes>0:
        seconds = seconds+60
        minutes-=1
    
    return seconds

def time_difference(hours1:int, minutes1:int, seconds1:int, hours2:int, minutes2:int, seconds2:int) -> int:
    if hours1>hours2:
        placeholder = hours1
        hours1 = hours2
        hours2 = placeholder
        placeholder = minutes1
        minutes1 = minutes2
        minutes2 = placeholder
        placeholder = seconds1
        seconds1 = seconds2
        seconds2 = placeholder
    hours = hours2-hours1
    minutes = minutes2-minutes1
    seconds = seconds2-seconds1
    print(hours)
    if minutes < 0:
        minutes +=60
        seconds -=3600
    print(hours)
    seconds = seconds_since_noon(hours, minutes, seconds)
    return seconds

print(time_difference(0, 0, 0, 12, 0, 0))

def rimbalzo() -> None:
    tempo: int = 0
    altezza: float = 0.0
    velocita: float = 100.0
    rimbalzi: int = 0
    print(f"Tempo: {tempo} Rimbalzo")
    while rimbalzi<6:
        tempo+=1
        altezza = altezza + velocita
        velocita = velocita - 96
        if altezza<0:
            print(f"Tempo: {tempo} Rimbalzo")
            velocita = velocita*-0.5
            altezza = altezza*-0.5
            rimbalzi +=1
        else:
            print(f"Tempo: {tempo} Altezza: {altezza}")

def rimbalzo() -> None:
    tempo: int = 0
    altezza: float = 0.0
    velocita: float = 100.0
    rimbalzi: int = 0
    while rimbalzi<5:
        if altezza<0:
            print(f"Tempo: {tempo} Rimbalzo! Velocità")
            altezza = altezza*-0.5
            velocita = velocita*-0.5
            rimbalzi +=1
        else:
            print(f"Tempo: {tempo} Altezza: {altezza}")
            altezza +=velocita
            velocita -=96
        tempo +=1

def memorizza_file(files: list[int]) -> None:
    spazio_totale_blocchi = 1000  # Spazio totale disponibile in blocchi
    for i in files:
        compresso=i*8/10
        if i % 512 == 0:
            spazio_occupato = compresso/512
        else:
            spazio_occupato = round(compresso/512)
        if spazio_totale_blocchi - spazio_occupato > 0:
            spazio_totale_blocchi -= spazio_occupato
            print(f"File di {i} byte compresso in {compresso} byte e memorizzato. Blocchi usati: {int(spazio_occupato)}. Blocchi rimanenti: {int(spazio_totale_blocchi)}.")
        else:
            print(f"Non è possibile memorizzare il file di {i} byte. Spazio insufficiente.")
            break
    
memorizza_file([1100, 20000, 1048576, 512, 5000])
